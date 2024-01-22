from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser

from shared.model.models import (
    CriteriaValidity,
    CPTCodes,
)


def get_structured_output_with_context_template(structured_output_parser, instructions):
    return PromptTemplate(
        template="""Given the following 'Context' about the medical patient, answer the query. 
                          Context: {context}
                          ##### END OF CONTEXT ##### 
                          Query: {query}
                          ##### END OF QUERY #####
                          Follow the instructions below to format your response.
                          Formatting instructions: {format_instructions}
                          {input_instructions}""",
        input_variables=["context", "query"],
        partial_variables={
            "format_instructions": structured_output_parser.get_format_instructions(),
            "input_instructions": instructions,
        },
    )


CRITERIA_VALIDY_INPUT_INSTRUCTIONS = """Assume that any medical/treatment history of the patient provided is complete and authoritative. 
In your response,'decision' should contain whether the given Query about the patient is true, false or uncertain. 
Respond with 'true' only when there is concrete evidence to support the statement. Respond with 'false' when there is concrete evidence against it. 
Respond with 'uncertain' if there is no information about the statement.
'reason' should contain the reason why you think the query is true/false/uncertain and the relevant section of the document that supports your answer."""

criteria_validity_parser = PydanticOutputParser(pydantic_object=CriteriaValidity)
criteria_validity_prompt_template = get_structured_output_with_context_template(
    criteria_validity_parser, CRITERIA_VALIDY_INPUT_INSTRUCTIONS
)

CPT_CODE_INPUT_INSTRUCTIONS = """Respond only with codes for requsted procedures in the treatment plan, not previously carried out procedures."""
cpt_code_parser = PydanticOutputParser(pydantic_object=CPTCodes)
cpt_code_prompt_template = get_structured_output_with_context_template(
    cpt_code_parser, CPT_CODE_INPUT_INSTRUCTIONS
)
