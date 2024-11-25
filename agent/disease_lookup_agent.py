
import os

from langchain import hub
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from tools.tools import get_profile_url_tavily
from tools.tools import  retrieve_psoriasis_info_from_web

load_dotenv()


def lookup(name: str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4o-mini",
        openai_api_key=os.environ["OPENAI_API_KEY"],
    )
    template = """given the disease name {name_of_disease} I want you to get it me one most current publication 
                    Your answer should contain a web page"""

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_disease"]
    )
    tools_for_agent = [
        Tool(
            name="Psoriasis information",
            func=retrieve_psoriasis_info_from_web,
            description="useful for when you need to get a web page",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_disease=name)}
    )

    psoriasis_page = result["output"]
    return psoriasis_page

if __name__ == "__main__":
    psoriasis_page = lookup(name ="psoriasis")
    print(psoriasis_page)