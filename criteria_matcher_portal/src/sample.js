const sample = {
    "reason": "Sub-criterias evaluate to uncertain",
    "decision": "uncertain",
    "criteria": {
      "conjunction_sub_criteria": [],
      "disjunction_sub_criteria": [
        {
          "reason": "Sub-criterias evaluate to false",
          "decision": "false",
          "criteria": {
            "conjunction_sub_criteria": [
              {
                "reason": "The patient's date of birth is 06/16/1982. As of the last update in the medical record, which is in 2023, the patient would be 41 years old.",
                "decision": "false",
                "criteria": {
                  "description": "Age 45 years or older"
                }
              },
              {
                "reason": "The patient's medical history does not mention any colonoscopy in the past 10 years. The only colonoscopy mentioned is scheduled for the future (12/15/2023).",
                "decision": "true",
                "criteria": {
                  "description": "No colonoscopy in past 10 years"
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
          "reason": "Sub-criterias evaluate to uncertain",
          "decision": "uncertain",
          "criteria": {
            "conjunction_sub_criteria": [],
            "disjunction_sub_criteria": [
              {
                "reason": "Sub-criterias evaluate to uncertain",
                "decision": "uncertain",
                "criteria": {
                  "conjunction_sub_criteria": [
                    {
                      "reason": "The patient's medical history does not mention any family history of colorectal cancer.",
                      "decision": "uncertain",
                      "criteria": {
                        "description": "Colorectal cancer diagnosed in one or more first-degree relatives of any age"
                      }
                    },
                    {
                      "reason": "The patient's date of birth is 06/16/1982. As of the last update in the medical record, which is in 2023, the patient would be 41 years old.",
                      "decision": "true",
                      "criteria": {
                        "description": "Age 40 years or older"
                      }
                    },
                    {
                      "reason": "The patient has been experiencing abdominal discomfort and rectal bleeding for the past 6 months, as stated in the 'PRESENTING COMPLAINT' section. However, there is no mention of iron deficiency anemia in the patient's medical history or diagnostic test results.",
                      "decision": "Uncertain",
                      "criteria": {
                        "description": "Symptomatic (eg, abdominal pain, iron deficiency anemia, rectal bleeding)"
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
                "reason": "The patient's family medical history is not mentioned in the provided context.",
                "decision": "uncertain",
                "criteria": {
                  "description": "Family member with colonic adenomatous polyposis of unknown etiology"
                }
              }
            ],
            "disjunction_condition": {
              "operator": ">=",
              "value": 1
            }
          }
        },
        {
          "reason": "Sub-criterias evaluate to false",
          "decision": "false",
          "criteria": {
            "conjunction_sub_criteria": [
              {
                "reason": "The patient's medical history and clinical impression do not mention or suggest a diagnosis of Juvenile polyposis syndrome. The patient has a history of appendectomy and knee arthroscopy, and is currently being evaluated for possible internal hemorrhoids, polyps, or colorectal cancer.",
                "decision": "false",
                "criteria": {
                  "description": "Juvenile polyposis syndrome diagnosis"
                }
              }
            ],
            "disjunction_sub_criteria": [
              {
                "reason": "The patient, James Freeman, was born on 06/16/1982, which makes him older than 12 years. He has been experiencing symptoms such as abdominal discomfort and rectal bleeding for the past 6 months. However, there is no mention of iron deficiency anemia or telangiectasia in the patient's medical history or symptoms.",
                "decision": "Uncertain",
                "criteria": {
                  "description": "Age 12 years or older and symptomatic (eg, abdominal pain, iron deficiency anemia, rectal bleeding, telangiectasia)"
                }
              },
              {
                "reason": "The patient's date of birth is 06/16/1982, which makes him older than 12 years. He has been experiencing symptoms such as abdominal discomfort and rectal bleeding. However, there is no mention of iron deficiency anemia or telangiectasia in the patient's medical history or presenting complaint.",
                "decision": "False",
                "criteria": {
                  "description": "Age younger than 12 years and symptomatic (eg, abdominal pain, iron deficiency anemia, rectal bleeding, telangiectasia)"
                }
              }
            ],
            "disjunction_condition": {
              "operator": ">=",
              "value": 1
            }
          }
        }
      ],
      "disjunction_condition": {
        "operator": ">=",
        "value": 1
      }
    }
  };
  
  export default sample;