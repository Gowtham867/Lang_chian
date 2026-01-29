from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama
import streamlit as st
llm=ChatOllama(model="llama3.2")
prompt=PromptTemplate(
    input_variables=["city","month","language","budget"],
    template="""
    Welcome to the {city} travel guide! 
    If you're visiting in {month}, here's what you can do: 
    1. Must-visit attractions. 
    2. Local cuisine you must try. 
    3. Useful phrases in {language}. 
    4. Tips for traveling on a {budget} budget. 
    Enjoy your trip!
"""
)
st.text("Travel Guide App")
city=st.text_input("Enter the city")
month=st.text_input("Enter no.of month")
lang=st.text_input("Enter language")
budget=st.selectbox("Travelling budget",["low","medium","high"])
chain=prompt | llm
if city and month and lang and budget:
    response=chain.invoke({"city":city,"month":month,"language":lang,"budget":budget})
    st.write(response.content)