#import os
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_community.chat_models import ChatOllama
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
import streamlit as st
#from langchain_google_genai import ChatGoogleGenerativeAI
#APIKEY=os.getenv("GOOGLE_API_KEY")
#llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite",api_key=APIKEY)
llm=ChatOllama(model="llama3.2")
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a python guide.Answer any questions related to the Python process"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human","{input}")
    ]
)
chain=prompt | llm
history_for_chain=StreamlitChatMessageHistory()
history_with_chain=RunnableWithMessageHistory(
    chain,
    lambda session_id:history_for_chain,
    input_message_key="input",
    history_messages_key="chat_history"
)
st.title("Python Guide")
qn=st.text_input("Enter the qn")

if qn:
    response=history_with_chain.invoke({"input":qn}, {"configurable":{"session_id":"goma1907"}})
    st.write(response.content)
st.write("HISTORY")
st.write(history_for_chain)