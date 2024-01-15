from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from criteria_store.prompt_config import (
    CRITERIA_PARSE_INSTRUCTIONS,
    CRITERIA_FEW_SHOT_EXAMPLES,
)

MODEL_NAME = "gpt-4"


class CriteriaParser:
    """Parses a raw criteria string into a Criteria object using an LLM"""

    @staticmethod
    def parse(criteria_cls, raw_criteria):
        criteria_parser = PydanticOutputParser(pydantic_object=criteria_cls)

        prompt = PromptTemplate(
            template="\n{format_instructions}\n{instructions}\n{few_shot_examples}\n{raw_criteria}\n###\n",
            input_variables=["raw_criteria"],
            partial_variables={
                "format_instructions": criteria_parser.get_format_instructions(),
                "instructions": CRITERIA_PARSE_INSTRUCTIONS,
                "few_shot_examples": CRITERIA_FEW_SHOT_EXAMPLES,
            },
        )

        model = ChatOpenAI(temperature=0, model=MODEL_NAME)

        chain = prompt | model | criteria_parser

        criteria_obj = chain.invoke({"raw_criteria": raw_criteria})
        return criteria_obj
