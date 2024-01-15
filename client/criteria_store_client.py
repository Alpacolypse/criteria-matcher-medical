import httpx
from shared.exceptions import (
    CriteriaNotFoundError,
    CriteriaStoreError,
)
import shared.model.models as models
import json


class CriteriaStoreClient:
    def __init__(
        self, base_url: str = "http://criteria_store_service:8000"
    ):  # TODO: Move to config. Modify this to localhost if running locally without docker-compose.
        self.base_url = base_url
        self.client = httpx.Client()

    def retrieve_criteria(self, criteria_type_id: str):
        try:
            response = self.client.get(
                f"{self.base_url}/criteria/retrieve/{criteria_type_id}", timeout=20
            )
            response.raise_for_status()
            criteria_content = json.loads(response.json())

            criteria_type = criteria_content["type"]
            criteria_data = criteria_content["data"]

            # Dynamically get the class based on type name
            # Assuming all criteria classes are defined in a module named 'criteria_models'
            criteria_class = getattr(models, criteria_type)

            # Deserialize the criteria object
            return criteria_class.parse_obj(criteria_data)
        except httpx.HTTPStatusError as e:
            status_code = e.response.status_code
            if status_code == 404:
                raise CriteriaNotFoundError(criteria_type_id)
            else:
                raise CriteriaStoreError(criteria_type_id)
        except Exception as e:
            raise CriteriaStoreError(criteria_type_id)
