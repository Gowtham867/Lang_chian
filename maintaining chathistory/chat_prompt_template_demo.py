from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama
import streamlit as st
llm=ChatOllama(model="llama3.2")
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a python Guide.Answer any question related to the Python"),
        ("human","{input}")
    ]
)
st.title("Python Guide")
qn=st.text_input("Enter the qn")

chain=prompt | llm
if qn:
    response=chain.invoke({"input":qn})
    st.write(response.content)