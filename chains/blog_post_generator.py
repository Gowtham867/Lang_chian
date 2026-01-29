from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama
import streamlit as st
from langchain_core.output_parsers import StrOutputParser
llm=ChatOllama(model="llama3.2")
title_prompt=PromptTemplate(
    input_variables=["topic"],
    template="""
    You are a professional blogger. 
    Create an outline for a blog post on the following topic: {topic} 
    The outline should include: 
    - Introduction 
    - 3 main points with subpoints 
    - Conclusion 
"""
)
speech_prompt=PromptTemplate(
    input_variables=["title"],
    template="""
    You are a professional blogger. 
    Write an engaging introduction paragraph based on the following 
    outline:{outline} 
    The introduction should hook the reader and provide a brief 
    overview of the topic.
"""
)

first_chain=title_prompt|llm|StrOutputParser()|(lambda title:(st.write(title),[title])[1])    #with title
second_chain=speech_prompt|llm
final_chain=first_chain|second_chain 

st.title("Blog Post Generator")
topic=st.text_input("Enter the topic")
if topic :
    response=final_chain.invoke({"topic":topic})
    st.write(response.content)