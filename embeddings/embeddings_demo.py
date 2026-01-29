from langchain_ollama import OllamaEmbeddings
llm=OllamaEmbeddings(model="nomic-embed-text")  #mxbai-embed-large    snowflake-arctic-embed
qn=input("Enter  the qn")
response=llm.embed_query(qn)
print(response)