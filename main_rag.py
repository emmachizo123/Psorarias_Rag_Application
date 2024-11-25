
"""
file holds our front end with Streamlit for the Psoriaris RAG BOT without Agent
"""
from typing import Set
#from backend.core import run_llm

from lookupllmwithagent import doLookup_with_LLM_Agent

import streamlit as st
from streamlit_chat import message

st.header("INIZIO  Psoraris RAG Application ")
prompt = st.text_input("Prompt", placeholder = "Enter Your Prompt here..")

# session persistence
#persist user prompt history. First iteration set it to an empty list

if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] =[]

#persist the chat history
if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] =[]




if prompt:
    with st.spinner("Generating Response"):
        generated_response =doLookup_with_LLM_Agent(name=prompt)

        #formatted_response =(
            #f"{generated_response['result']} "
        #)


        st.session_state["user_prompt_history"].append(prompt)
        #st.session_state["chat_answers_history"].append(formatted_response)
        st.session_state["chat_answers_history"].append(dict(generated_response)["content"])

if st.session_state["chat_answers_history"]:
    for generated_response,user_query in zip( st.session_state["chat_answers_history"],st.session_state["user_prompt_history"]):
        message(user_query, is_user=True)
        message(generated_response)




