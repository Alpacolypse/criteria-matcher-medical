from langchain_core.prompts import PromptTemplate, format_document
from treatment_evaluation.prompt_templates import (
    cpt_code_prompt_template,
    cpt_code_parser,
)
DEFAULT_DOCUMENT_PROMPT = PromptTemplate.from_template(template="{page_content}")

MAX_DOCUMENT_LIMIT = 4  ## Needs to be fine tuned

def combine_documents(
    docs, document_prompt=DEFAULT_DOCUMENT_PROMPT, document_separator="###\n\n"
):
    doc_strings = [format_document(doc, document_prompt) for doc in docs]
    return document_separator.join(doc_strings[:MAX_DOCUMENT_LIMIT])


def get_criteria_type(record_knowledge_base):

    query = "What is/are the CPT code(s) for the requested procedure(s) suggested for this patient?"
    relevant_documents = record_knowledge_base.get_relevant_documents(query)

    chain = cpt_code_prompt_template | record_knowledge_base.model | cpt_code_parser

    return chain.invoke({"context": relevant_documents, "query": query})
