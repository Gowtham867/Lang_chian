from langchain_ollama import OllamaEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
llm=OllamaEmbeddings(model="nomic-embed-text") 
document=TextLoader("job_listings.txt").load()
text_splitter=RecursiveCharacterTextSplitter(chunk_size=200,chunk_overlap=10)
chunks=text_splitter.split_documents(document)
db=FAISS.from_documents(chunks,llm)
retriver=db.as_retriever()
qn=input("Enter  the qn ")
# embeddings_vector=llm.embed_query(qn)
# docs=db.similarity_search_by_vector(embeddings_vector)
docs=retriver.invoke(qn)
for doc in docs:
    print(doc.page_content)