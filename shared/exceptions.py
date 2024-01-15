class CriteriaNotFoundError(Exception):
    def __init__(self, criteria_type_id):
        self.criteria_type_id = criteria_type_id
        self.message = f"Criteria with id {criteria_type_id} not found"
        super().__init__(self.message)


class CriteriaStoreError(Exception):
    def __init__(self, criteria_type_id):
        self.criteria_type_id = criteria_type_id
        self.message = f"Error retrieving {criteria_type_id} from store"
        super().__init__(self.message)


class InternalServerError(Exception):
    def __init__(self, message="Internal server error"):
        self.message = message
        super().__init__(self.message)
