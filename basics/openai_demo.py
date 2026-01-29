import os
from langchain_openai import ChatOpenAI
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
llm=ChatOpenAI(model="gpt-4o",api_key=OPENAI_API_KEY)
qn=input("Enter  the qn")
response=llm.invoke(qn)
print(response.content)