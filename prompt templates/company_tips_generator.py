from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama
import streamlit as st
llm=ChatOllama(model="gemma:2b")
prompt=PromptTemplate(
    input_variables=["Company","Position","Strengths","Weaknesses"],
    template="""
    You are a career coach. Provide tailored interview tips for the 
    position of {Position} at {Company}. 
    Highlight your strengths in {Strengths} and prepare for questions 
    about your weaknesses such as {Weaknesses}.
"""
)
st.title("Interview helper")
company=st.text_input("Enter company name")
position=st.text_input("Enter position")
strengths=st.text_area("Enter your strengths",height=100)
weaknesses=st.text_area("Enter your weaknesses",height=100)
if company and position and strengths and weaknesses:
    final_prompt=prompt.format(Company=company,Position=position,Strengths=strengths,Weaknesses=weaknesses)
    response=llm.invoke(final_prompt)
    st.write(response.content)
