import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
llm=ChatOllama(model="llama3.2")
prompt=PromptTemplate(
    input_variables=["player"],
    template="""
    Explain the cricket player {player} in simple worsds
    include:
    playing role
    major achievements
    carrer highlights 
    total number of half-centuries and centuries till datess
"""
)
st.title("History of cricketers")
name=st.text_input("Enter player name")
if name:
    final_text=prompt.format(player=name)
    response=llm.invoke(final_text)
    st.write(response.content)