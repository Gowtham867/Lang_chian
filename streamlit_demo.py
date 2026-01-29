
from langchain_community.chat_models import ChatOllama
import streamlit as st
from langchain_core.globals import set_debug
set_debug(True)
st.title("Ask anything")
with st.sidebar:
    st.title("provide your base url")
    baseurl=st.text_input("Baseurl",type="password")
if not baseurl:
    st.info("Enter your base url to continue")
    st.stop()
llm = ChatOllama(
    model="qwen2.5:1.5b",
    base_url=baseurl)

qn=st.text_input("Enter the qn: ")
if qn:
    response=llm.invoke(qn)
    st.write(response.content)