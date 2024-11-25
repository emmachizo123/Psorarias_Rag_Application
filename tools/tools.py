
from langchain_community.utilities import SerpAPIWrapper
from langchain_community.tools.tavily_search import TavilySearchResults
import os
from dotenv import load_dotenv
from openai import api_key

load_dotenv()




def retrieve_psoriasis_info_from_web(query:str):
    """searches for psoriasis info on the web"""
    api_key= os.getenv("SERPAPI_API_KEY")
    print(f"print the key{api_key}")
    #search = SerpAPIWrapper (api_key=f'{os.environ.get("SERPAPI_API_KEY")}')
    search = SerpAPIWrapper()

    results= search.run(f"{query}")
    return results


def get_profile_url_tavily(name:str):
    """searches for Linkedin or Twitter Profile page"""

    search =TavilySearchResults()
    res= search.run(f"{name}")
    return res