# from langchain_core.prompts import PromptTemplate
# prompt_template=PromptTemplate(
#     input_variables=["topic"],
#     template="Explain {topic} in simple words"
# )
# formatted_prompt = prompt_template.format(topic="LangChain")
# print(formatted_prompt)


# from langchain_core.prompts import PromptTemplate
# from langchain_community.chat_models import ChatOllama
# import streamlit as st
# llm=ChatOllama(model="gemma:2b")
# prompt=PromptTemplate(
#     input_variables=["country","paras","language"],
#     template="""
#     You are an expert in traditional cuisines. 
#     You provide information about a specific dish from a specific country. 
#     Avoid giving information about fictional places. If the country is fictional 
#     or non-existent answer: I don't know. 
#     Answer the question: What is the traditional cuisine of {country}? 
#     Answer in {paras} short paras in {language}
# """
# )
# st.title("Cusine Info")
# country=st.text_input("Enter the country")
# paras=st.number_input("Enter no.of paras",min_value=1,max_value=5)
# lang=st.text_input("Enter language")
# if country and paras and lang:
#     final_prompt=prompt.format(country=country,paras=paras,language=lang)
#     response=llm.invoke(final_prompt)
#     st.write(response.content)  



# from langchain_core.prompts import PromptTemplate
# from langchain_community.chat_models import ChatOllama
# import streamlit as st
# llm = ChatOllama(model="llama3.2")
# prompt = PromptTemplate(
#     input_variables=["country", "paras", "language", "history"],
#     template="""
#         You are an expert in traditional cuisines.
#         Conversation history:
#         {history}
#         Now answer the new question below based on general knowledge.
#         Question:
#         What is the traditional cuisine of {country}?
#         IMPORTANT:
#         - The answer MUST be written ONLY in {language}.
#         - Write {paras} short paragraphs.
#     """
# )
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []
# st.title("Cuisine Info")
# st.write("### Chat History")
# for role, msg in st.session_state.chat_history:
#     st.write(f"**{role}:** {msg}")
# country = st.text_input("Enter the country")
# paras = st.number_input("Enter no. of paras", min_value=1, max_value=5)
# language = st.text_input("Enter language")
# if country and paras and language:
#     history_text = ""
#     for role, msg in st.session_state.chat_history:
#         history_text += f"{role}: {msg}\n"
#     final_prompt = prompt.format(
#         country=country,
#         paras=paras,
#         language=language,
#         history=history_text
#     )
#     response = llm.invoke(final_prompt).content
#     st.session_state.chat_history.append(("User", f"country:{country} |language: {language}"))
#     st.session_state.chat_history.append(("AI", response))
#     st.write(response)




from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama
import streamlit as st
llm = ChatOllama(model="llama3.2")
prompt = PromptTemplate(
    input_variables=["country", "paras", "language", "history"],
    template="""
        You are an expert in traditional cuisines.
        Conversation history:
        {history}
        Now answer the new question below based on general knowledge.
        Question:
        What is the traditional cuisine of {country}?
        IMPORTANT:
        - The answer MUST be written ONLY in {language}.
        - Write {paras} short paragraphs.
"""
)
history_query_prompt = PromptTemplate(
    input_variables=["history", "query"],
    template="""
        You are given the following conversation history:
        {history}
        User query:
        {query}
        INSTRUCTIONS:
        - Answer the query using ONLY the information present in the history.
        - Do NOT add new facts.
        - If the answer is not present in history, say:
        "Not available in previous chat history."
"""
)
def query_from_chat_history(chat_history, query):
    history_text = ""
    for role, msg in chat_history:
        history_text += f"{role}: {msg}\n"

    final_prompt = history_query_prompt.format(
        history=history_text,
        query=query
    )
    return llm.invoke(final_prompt).content
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
st.title("Cuisine Info")
st.write("### Chat History")
for role, msg in st.session_state.chat_history:
    st.write(f"**{role}:** {msg}")
country = st.text_input("Enter the country")
paras = st.number_input("Enter no. of paras", min_value=1, max_value=5)
language = st.text_input("Enter language")
query = st.text_input("Ask something from previous chat history")
if query:
    answer = query_from_chat_history(
        st.session_state.chat_history,
        query
    )
    st.subheader("Answer from Chat History")
    st.write(answer)
if country and paras and language:
    history_text = ""
    for role, msg in st.session_state.chat_history:
        history_text += f"{role}: {msg}\n"
    final_prompt = prompt.format(
        country=country,
        paras=paras,
        language=language,
        history=history_text
    )
    response = llm.invoke(final_prompt).content
    st.session_state.chat_history.append(
        ("User", f"country:{country} | language:{language}")
    )
    st.session_state.chat_history.append(("AI", response))
    st.subheader("AI Response")
    st.write(response)
