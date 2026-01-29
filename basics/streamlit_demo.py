from langchain_community.chat_models import ChatOllama
import streamlit as st
from langchain_core.globals import set_debug
set_debug(True)
llm=ChatOllama(model="gemma:2b")
st.title("Ask anything")
qn=st.text_input("Enter the qn: ")
if qn:
    response=llm.invoke(qn)
    st.write(response.content)