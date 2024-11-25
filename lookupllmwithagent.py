
import os
from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from pathlib import Path

from IngestToDatabase import fetch_file_content_by_name

#import our lookup agent
from agent.psoriasis_lookup_agent import lookup as Psoriaris_lookup_agent

from agent.disease_lookup_agent import lookup as Disease_lookup_agent



# Read the data context into a variable

def doLookup_with_LLM_Agent(name:str)->str:
    #calling the psoriasis_look_up_agent
    #psoriaris_page_name = Psoriaris_lookup_agent(name=name)
    disease_page_name = Psoriaris_lookup_agent(name=name)

    # create the summary_template which is an output indicator to narrow down our result
    # make it definitive
    summary_template = """
            given the information {information} about psoriasis I want you to create 
            1. a short summary
            2. generate 5 questions from the information

        """
    # Inititialise prompt template
    # input_variable is the input we will plug in dynamically
    # PromptTemplate object takes the input  and the template is the text before we inject it with the
    # variable
    summary_prompt_template = PromptTemplate(
        input_variable=["information"], template=summary_template
    )

    # a variable to hold an instance of ChatOpenAI
    # chat models are wrappers around the langauge models
    # temperature decides how creative the language model will be

    print("key is " + str(os.environ.get("OPENAI_API_KEY")))

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", api_key=f'{os.environ.get("OPENAI_API_KEY")}')

    #create the chain
    chain = summary_prompt_template | llm

    #res = chain.invoke(input={"information": psoriaris_page_name})
    res = chain.invoke(input={"information": disease_page_name})
    return res





if __name__ == "__main__":
    load_dotenv()
    print("LookupllmWithAgent")
    doLookup_with_LLM_Agent(name="psoriaris")






