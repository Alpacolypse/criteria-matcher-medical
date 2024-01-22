# from langchain_core.pydantic_v1 import BaseModel, Field
from pydantic import BaseModel, Field
from typing import List, Union, Optional


class CriteriaInput(BaseModel):
    id: str
    criteria: str


class CPTCodes(BaseModel):
    codes: List[str] = Field(
        description="The CPT code(s) for the treatment plan or procedure suggested for this patient. Only return codes for proposed/requested procedures in the treatment plan."
    )


class DisjunctionCondition(BaseModel):
    operator: str = Field(
        description="The operator to use to compare the number of true sub_criteria with the value. One of '>=', '<=', '>', '<', '==', '!='"
    )
    value: int = Field(
        description="The value to compare the number of true sub_criteria with"
    )


class CriteriaPredicate(BaseModel):
    description: str = Field(
        description="The statement of the criteria to be checked for"
    )


class SubCriteria(BaseModel):
    conjunction_sub_criteria: List["Criteria"] = Field(
        description="The criteria that must all be true for this criteria to be true. Can be an empty list."
    )
    disjunction_sub_criteria: List["Criteria"] = Field(
        description="The criteria of which at least some must be true for this criteria to be true. Can be an empty list."
    )
    disjunction_condition: DisjunctionCondition | None = Field(
        description="The condition that the number of true disjunction_sub_criteria must meet."
    )


class Criteria(BaseModel):
    criteria: Union[CriteriaPredicate, SubCriteria] = Field(
        description="Either a CriteriaPredicate or a SubCriteria"
    )


SubCriteria.update_forward_refs()


# OUTPUTS


class CriteriaValidity(BaseModel):
    reason: str = Field(description="The reason and context for the decision")
    decision: str = Field(
        description="Whether the criteria is 'true', 'false' or 'uncertain'"
    )


class CriteriaPredicateOut(BaseModel):
    description: str = Field(
        description="The statement of the criteria to be checked for"
    )


class SubCriteriaOut(BaseModel):
    conjunction_sub_criteria: List["CriteriaOut"] = Field(
        description="The list of criteria that must all be true for this criteria to be true. Can be an empty list."
    )
    disjunction_sub_criteria: List["CriteriaOut"] = Field(
        description="The list criteria of which at least some must be true for this criteria to be true. Can be an empty list."
    )
    disjunction_condition: DisjunctionCondition = Field(
        description="The condition that the number of true disjunction_sub_criteria must meet."
    )


class CriteriaOut(CriteriaValidity):
    criteria: Union[CriteriaPredicateOut, SubCriteriaOut] = Field(
        description="Either a CriteriaPredicateOut or a SubCriteriaOut"
    )


SubCriteriaOut.update_forward_refs()


class TreatmentEvaluationResponse(BaseModel):
    code: str = Field(
        description="The CPT code(s) for the treatment plan or procedure suggested for this patient."
    )
    criteria_tree: Optional[CriteriaOut] = Field(
        description="The criteria that was evaluated, or a string indicating that criteria was not found"
    )
