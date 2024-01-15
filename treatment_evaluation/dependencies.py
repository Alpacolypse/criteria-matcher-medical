from treatment_evaluation.orchestrator import Orchestrator
from treatment_evaluation.matcher import CriteriaMatcher
from client.criteria_store_client import CriteriaStoreClient
from langchain_openai import ChatOpenAI
from fastapi import Depends


def get_llm_model():
    return ChatOpenAI(temperature=0, model="gpt-4")


def get_criteria_store_client():
    return CriteriaStoreClient()


def get_criteria_matcher(model=Depends(get_llm_model)):
    return CriteriaMatcher(model=model)


def get_orchestrator(
    criteria_store_client=Depends(get_criteria_store_client),
    criteria_matcher=Depends(get_criteria_matcher),
):
    return Orchestrator(
        criteria_store_client=criteria_store_client, criteria_matcher=criteria_matcher
    )
