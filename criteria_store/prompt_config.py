CRITERIA_PARSE_INSTRUCTIONS = """
Formulate the criteria from the given text. 
Each criteria must either be a CriteriaPredicate or a SubCriteria. 
The CriteriaPredicate must contain a field 'description' which describes the condition for the given criteria. 
The SubCriteria contains a list of conjunction_sub_criteria , a list of disjunction sub_criteria (OR) and a disjunction_condition.
The conjunction_sub_criteria are the criteria that must all be true for this criteria to be true. It could be an empty list, but it should always be present in the response.
The disjunction_sub_criteria are the criteria of which at least some must be true for this criteria to be true. It could be an empty list, but it should always be present in the response.
The disjunction_condition has an operator and a value. The operator is one of '>=', '<=', '>', '<', '==', '!='. The value is a number. It denotes the condition that the number of true disjunction_sub_criteria must meet for this criteria to be true.
For e.g "5 or more of the following are true" would be represented as operator='>=' and value=5.
The SubCriteria is considered to be satisfied only when all of the conjunction_sub_criteria are true, and the number of true disjunction_sub_criteria meet the disjunction_condition.
"""

CRITERIA_FEW_SHOT_EXAMPLES = """
---
Input:
• Type 2 Diabetes management, as indicated by 1 or more of the following:
o Patient diagnosed with Type 2 Diabetes, as indicated by ALL of the following:
§ HbA1c level of 6.5% or higher
§ Fasting blood sugar level of 126 mg/dL or higher
o Diabetes diagnosed in one or more first-degree relatives of any age and 2 of the thefollowing:
§ History of cardiovascular disease
§ Presence of kidney disease or microalbuminuria
§ Diabetic retinopathy or neuropathy
o Patients not meeting targets on current management plan, indicated by:
§ HbA1c level above the target range set by the physician
§ Uncontrolled blood sugar levels despite current medication regimen
###
{
        "criteria": {
            "conjunction_sub_criteria": [],
            "disjunction_sub_criteria": [
                {
                    "criteria": {
                        "conjunction_sub_criteria": [
                            {
                                "criteria": {
                                    "description": "HbA1c level of 6.5% or higher"
                                }
                            },
                            {
                                "criteria": {
                                    "description": "Fasting blood sugar level of 126 mg/dL or higher"
                                }
                            }
                        ],
                        "disjunction_sub_criteria": [],
                        "disjunction_condition": {
                            "operator": "==",
                            "value": 0
                        }
                    }
                },
                {
                    "criteria": {
                        "conjunction_sub_criteria": [
                            {
                                "criteria": {
                                    "description": "Diabetes diagnosed in one or more first-degree relatives of any age"
                                }
                            }
                        ],
                        "disjunction_sub_criteria": [
                            {
                                "criteria": {
                                    "description": "History of cardiovascular disease"
                                }
                            },
                            {
                                "criteria": {
                                    "description": "Presence of kidney disease or microalbuminuria"
                                }
                            },
                            {
                                "criteria": {
                                    "description": "Diabetic retinopathy or neuropathy"
                                }
                            }
                        ],
                        "disjunction_condition": {
                            "operator": ">=",
                            "value": 2
                        }
                    }
                },
                {
                    "criteria": {
                        "conjunction_sub_criteria": [
                            {
                                "criteria": {
                                    "description": "HbA1c level above the target range set by the physician"
                                }
                            },
                            {
                                "criteria": {
                                    "description": "Uncontrolled blood sugar levels despite current medication regimen"
                                }
                            }
                        ],
                        "disjunction_sub_criteria": [],
                        "disjunction_condition": {
                            "operator": "==",
                            "value": 0
                        }
                    }
                }
            ],
            "disjunction_condition": {
                "operator": ">=",
                "value": 1
            }
        }
    }
---
Input:"""
