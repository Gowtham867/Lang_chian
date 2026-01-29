from langchain_ollama import OllamaEmbeddings
embeddings=OllamaEmbeddings(model="nomic-embed-text")  
response=embeddings.embed_documents(
   [ 'good',
    'better',
    'best',
    'bad',
    'worse',
    'worst']
)
print(len(response))
print(response[0])