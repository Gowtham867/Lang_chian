import os
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain.chains import create_retrieval_chain,create_history_aware_retriever
from langchain.chains.combine_documents import create_stuff_documents_chain
from dotenv import load_dotenv
import streamlit as st
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
load_dotenv()
model_name = os.getenv("ollama_model")
ollama_url = os.getenv("ollama_url")
llm = ChatOllama(model=model_name, base_url=ollama_url)
embeddings=OllamaEmbeddings(model="nomic-embed-text") 
document=TextLoader("product-data.txt").load()
text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
chunks=text_splitter.split_documents(document)
vector_store=Chroma.from_documents(chunks,embeddings)
retriver=vector_store.as_retriever()
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","""
    You are an assistant for answering questions. 
    Use the provided context to respond.If the answer  
    isn't clear, acknowledge that you don't know.  
    Limit your response to three concise sentences. 
    {context}
    """),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human","{input}")
    ]
)
history_aware_retriever=create_history_aware_retriever(llm,retriver,prompt)
qa_chain=create_stuff_documents_chain(llm,prompt)
rag_chain=create_retrieval_chain(history_aware_retriever,qa_chain)
history_for_chain=StreamlitChatMessageHistory()
history_with_chain=RunnableWithMessageHistory(
    rag_chain,
    lambda session_id:history_for_chain,
    input_message_key="input",
    history_messages_key="chat_history"
)
st.write("chat with document")
qn=st.text_input("Enter qn ")
response=history_with_chain.invoke({"input":qn},{"configurable":{"session_id":"goma1907"}})
st.write(response['answer'])
