
# Criteria Matcher

`criteria_matcher` provides two APIs:

1. `/criteria/ingest`: This API takes a set of text-based human language guidelines and maps them to a partial formal logic structure.
2. `/evaluate-treatment-plan/`: This API takes a PDF of a medical record and tries to match the requested criteria against the record. It outputs a verbose tree of nested criteria and sub-criteria with reasoning as to why each individual predicate was a match or not. If it's not able to ascertain the truth of a given predicate, it indicates the same.

## Steps to Run

In the root directory:

- Create a `local.env` file and supply your `OPENAI_API_KEY`:

  ```
  OPENAI_API_KEY=<key>
  ```

- Build and run the application using Docker:

  ```
  docker-compose build
  docker-compose up
  ```

The `criteria_store_service` API should be running at `http://127.0.0.1:8000/docs`. 

Here you can upload criteria in natural language and the code that it should map to.

**Example Input:**

```json
{
  "id": "45378",
  "criteria": "• Colorectal cancer screening, as indicated by 1 or more of the following:\n\to Patient has average-risk or higher, as indicated by ALL of the following\n\t\t§ Age 45 years or older\n\t\t§ No colonoscopy in past 10 years\n\to High risk family history, as indicated by 1 or more of the following:\n\t\t§ Colorectal cancer diagnosed in one or more first-degree relatives of any age and ALL of the following:\n\t\t\t• Age 40 years or older\n\t\t\t• Symptomatic (eg, abdominal pain, iron deficiency anemia, rectal bleeding)\n\t\t§ Family member with colonic adenomatous polyposis of unknown etiology\n\to Juvenile polyposis syndrome diagnosis AND 1 or more of the following:\n\t\t§ Age 12 years or older and symptomatic (eg, abdominal pain, iron deficiency anemia, rectal bleeding,\ntelangiectasia)\n\t\t§ Age younger than 12 years and symptomatic (eg, abdominal pain, iron deficiency anemia, rectal bleeding,\ntelangiectasia)"
}
```

(In case you get a 500 error, retry a few times.)

The `treatment_evaluation_service` API should be running at `http://127.0.0.1:8080/docs`.

Upload a medical record PDF. If the record contains a CPT code for which treatment has been requested, and for which you have uploaded criteria for, you’ll get a response that looks like:

```json
[
  {
    "code": "45378",
    "criteria_tree": {
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
    }
  }
]
```

A criteria can either be - 
1. A leaf level (aka without any sub-criteria) predicate. It evalutes to true when the predicate is true for the given medical record. 
2. A criteria with nested conjunction (necessary) and disjunction (optional) sub-criteria. This type of criteria is true if all the conjunction sub-criteria are true and if the number of true disjunction criteria match the disjunction condition. 
For e.g "A must be true but only one of B or C must be true" translates to - 

```
conjunction_sub_criteria: [A]
disjunction_sub_critiera: [B,C]
disjunctrion_sub_condition: operator="==", value=1
```


HLD :
![criteria_matcher_medical_10000ft](https://github.com/Alpacolypse/criteria-matcher-medical/assets/128543722/15764887-9770-4d98-94ac-dfc925366a3e)


