from treatment_evaluation.record_knowledge_base import RecordKnowledgeBase
from shared.model.models import CriteriaOut, TreatmentEvaluationResponse
from shared.exceptions import CriteriaNotFoundError, CriteriaStoreError
from devtools import debug


class Orchestrator:
    def __init__(self, criteria_store_client, criteria_matcher):
        self.criteria_store_client = criteria_store_client
        self.criteria_matcher = criteria_matcher

    def evaluate_record(self, file_path):
        # Create knowledge base from medical record
        record_knowledge_base = RecordKnowledgeBase(file_path)

        # Retrieve criteria_type_ids (CPTCodes, in this case) ids from record
        criteria_type_ids = record_knowledge_base.criteria_type

        result = []
        for criteria_type_id_code in criteria_type_ids.codes:
            try:
                # Retrieve criteria from store
                criteria = self.criteria_store_client.retrieve_criteria(
                    criteria_type_id_code
                )

                # Match criteria to record
                criteria_out = self.criteria_matcher.match(
                    criteria, record_knowledge_base
                )
                debug(criteria_out)

                # Construct response
                treatment_evaluation_response = TreatmentEvaluationResponse(
                    code=criteria_type_id_code, criteria_tree=criteria_out
                )
                result.append(treatment_evaluation_response)

            except CriteriaNotFoundError as e:
                result.append(
                    TreatmentEvaluationResponse(
                        code=criteria_type_id_code, criteria_tree=None
                    )
                )

        return result
