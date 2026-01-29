import os
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from dotenv import load_dotenv
load_dotenv()
model_name = os.getenv("ollama_model")
ollama_url = os.getenv("ollama_url")
llm = ChatOllama(model=model_name, base_url=ollama_url)
#llm=ChatOllama(model="llama3.2")
embeddings=OllamaEmbeddings(model="nomic-embed-text") 
document=PyPDFLoader("academic_research_data.pdf").load()
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
        ("human","{input}")
    ]
)
qa_chain=create_stuff_documents_chain(llm,prompt)
rag_chain=create_retrieval_chain(retriver,qa_chain)
print("chat with document")
qn=input("Enter qn ")
response=rag_chain.invoke({"input":qn})
print(response['answer'])
