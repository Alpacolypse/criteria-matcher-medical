from fastapi import FastAPI, HTTPException, Depends
from criteria_store.criteria_parser import CriteriaParser
from shared.model.models import Criteria
from criteria_store.dependencies import get_criteria_store
from shared.exceptions import CriteriaNotFoundError
from fastapi.middleware.cors import CORSMiddleware
from shared.model.models import CriteriaInput
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/criteria/ingest/")
def ingest(criteria_in: CriteriaInput, criteria_store=Depends(get_criteria_store)):
    try:
        # Parse the criteria string to a Criteria object
        criteria_obj: Criteria = CriteriaParser.parse(Criteria, criteria_in.criteria)

        criteria_store.insert_criteria(criteria_in.id, criteria_obj)

        return criteria_obj
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="Failed to ingest criteria, internal server error"
        )


@app.get("/criteria/retrieve/{id}")
def retrieve(id: str, criteria_store=Depends(get_criteria_store)):
    try:
        # Load the JSON from the file
        return criteria_store.get_criteria(id)

    except CriteriaNotFoundError:
        raise HTTPException(status_code=404, detail="Criteria not found")
    except Exception as e:
        # TODO: log the error
        raise HTTPException(
            status_code=500, detail="Failed to retrieve criteria, Internal server Error"
        )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
