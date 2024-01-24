from generic_criteria_matcher.document_knowledge_base import DocumentKnowledgeBase
from devtools import debug

class Orchestrator:
    def __init__(self, criteria_matcher, criteria_parser):
        self.criteria_matcher = criteria_matcher
        self.criteria_parser = criteria_parser

    def evaluate_document(self, raw_criteria, file_path):
        # Create knowledge base from medical record
        record_knowledge_base = DocumentKnowledgeBase(file_path)

        criteria = self.criteria_parser.parse_raw(raw_criteria)
        
        criteria_out = self.criteria_matcher.match(
            criteria, record_knowledge_base
        )

        debug(criteria_out)
        return criteria_out
    
    
