import numpy as np
from langchain_ollama import OllamaEmbeddings
llm=OllamaEmbeddings(model="nomic-embed-text")  #llama3.2   mxbai-embed-large    snowflake-arctic-embed
qn1=input("Enter the qn1 ")
qn2=input("Enter the qn2 ")
response1=llm.embed_query(qn1)
response2=llm.embed_query(qn2)
similarity_score=np.dot(response1,response2)
print(similarity_score)
print(similarity_score*100,'%')