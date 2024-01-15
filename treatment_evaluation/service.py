from tempfile import NamedTemporaryFile
import os
from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from shared.exceptions import CriteriaNotFoundError
from shared.model.models import TreatmentEvaluationResponse
from fastapi.middleware.cors import CORSMiddleware
from treatment_evaluation.dependencies import get_orchestrator
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/evaluate-treatment-plan/")
async def evaluate_treatment_plan(
    file: UploadFile = File(...), orchestrator=Depends(get_orchestrator)
):
    # Create a temporary file to save the uploaded PDF
    with NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        content = await file.read()
        temp_file.write(content)
        temp_file_path = temp_file.name

    try:
        return orchestrator.evaluate_record(temp_file_path)
    except CriteriaNotFoundError:
        raise HTTPException(status_code=404, detail="Criteria not found")

    finally:
        # Clean up: delete the temporary file
        os.remove(temp_file_path)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
