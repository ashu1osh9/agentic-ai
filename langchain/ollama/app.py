import os
from dotenv import load_dotenv
load_dotenv()
from langchain_community.chat_models import ChatOllama 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

# LANGHCAIN TRACKING 
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

# LLM MODEL
model=ChatOllama(model="llama3.1:8b")

# chatprompttemplets
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the question asked"),
        ("user","Question:{question}")
    ]
)

#stroutputs parse
outputs=StrOutputParser()
chain = prompt|model|outputs

#streamlit
st.title("Welcome to the ai world.")
inputs_text=st.text_input("whats on your mind")

if inputs_text:
    st.write(chain.invoke({"question":inputs_text}))



