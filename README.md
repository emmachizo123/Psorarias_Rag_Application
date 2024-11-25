README

Application Name : Psorarias_Rag_Application

Brief Summary 

The task involves developing a basic Retrieval-Augmented Generation (RAG) 
system using agents for data retrieval and processing, with a FastAPI frontend 
for interaction. 
In this task you will have an opportunity to demonstrate core data engineering skills, 
agent-based system development, API creation, and rapid prototyping. 
This application is a prototyping a platform which will allow users to perform two actions 
on top of publication data related to psoriasis. 
Users will be allowed to search psoriasis data using natural language 
and allow them to create multiple choice questions from the same data. 

 

Installation
To install the project simply clone the repository and install the dependencies using the following steps:

git clone https://github.com/emmachizo123/Psorarias_Rag_Application

cd Psorarias_Rag_Application

pip install -r requirements.txt

create .env file 


Setup Streamlit  
This current version uses Streamlit as the frontend
The entry point for the aplication is main_rag.py
Setup a Streamlit Frontend using main_rag.py