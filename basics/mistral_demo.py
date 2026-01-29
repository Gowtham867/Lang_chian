from langchain_community.chat_models import ChatOllama
llm=ChatOllama(model="mistral")
qn=input("Enter  the qn")
response=llm.invoke(qn)
print(response.content)