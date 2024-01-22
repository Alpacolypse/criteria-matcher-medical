from langchain_core.pydantic_v1 import BaseModel
from data.sample_criteria import COLONOSCOPY_CRITERIA
from shared.exceptions import CriteriaNotFoundError
import os
import json

class CriteriaStore:

    def insert_criteria(self, criteria_type_id: str, criteria_obj: BaseModel):
        # Define the directory path
        dir_path = "data/parsed_criteria"
        os.makedirs(
            dir_path, exist_ok=True
        )  # Create the directory if it does not exist

        # Define the full file path
        file_path = os.path.join(dir_path, f"{criteria_type_id}.json")

        # Include type information
        data_to_save = {
            "type": type(criteria_obj).__name__,
            "data": criteria_obj.dict(),
        }

        # Serialize and Write the data to a file
        with open(file_path, "w") as file:
            json.dump(data_to_save, file, indent=4)

    def get_criteria(self, criteria_type_id: str):
        try:
            dir_path = "data/parsed_criteria"
            file_path = os.path.join(dir_path, f"{criteria_type_id}.json")

            # Load the JSON from the file
            with open(file_path, "r") as file:
                criteria_json = file.read()
                return criteria_json
        except FileNotFoundError:
            raise CriteriaNotFoundError(criteria_type_id)
