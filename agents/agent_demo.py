import os
import streamlit as st
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate
from langchain_core.globals import set_debug

load_dotenv()
set_debug(True)

st.title("AI Agent with Ollama")

llm = ChatOllama(
    model=os.getenv("ollama_model"),
    base_url=os.getenv("ollama_url"),
    stop=["\nObservation:", "\nThought:", "\nAction:"]
)

tools = [
    DuckDuckGoSearchRun(
        name="search",
        description="Search the web for answers"
    )
]

prompt = PromptTemplate.from_template(
        """You are a helpful AI agent.
        You have access to the following tools:
        {tools}
        Tool names:
        {tool_names}
        You must follow this format EXACTLY:
        Thought: your reasoning
        Action: the tool name (ONLY if a tool is needed)
        Action Input: the input to the tool
        OR
        Final Answer: the final answer
        Rules:
        - Use ONLY the tool names provided
        - NEVER explain the format
        - NEVER invent tools
        user task:
        {input}
        {agent_scratchpad}
        """)

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=1,          
    max_execution_time=200,
)

user_input = st.text_input("Ask me anything")

if st.button("Submit"):
    result = agent_executor.invoke({"input": user_input})
    st.write(result["output"])



# import os
# import streamlit as st
# from dotenv import load_dotenv
 
# from langchain_ollama import ChatOllama
 
# from langchain_community.tools import DuckDuckGoSearchRun
# from langchain.agents import create_react_agent
# from langchain.agents import AgentExecutor
# from langchain_core.prompts import PromptTemplate
# from langchain_core.globals import set_debug
 
 
# load_dotenv()
# set_debug(True)
 
# st.set_page_config(page_title="Ollama Python Agent", layout="wide")
# st.title("🚀 Ollama Python Code Agent")
 
# ollama_model = os.getenv("ollama_model")
# ollama_url = os.getenv("ollama_url")
 
 
# llm = ChatOllama(
#     model=ollama_model,
#     base_url=ollama_url
# )
 
 
 
# tools = [
#     DuckDuckGoSearchRun(
#         name="search",
#         description="Search the web for Python libraries, APIs, or examples"
#     )
# ]
 
 
# prompt = PromptTemplate.from_template("""
# You are a senior Python engineer using the ReAct pattern.
 
# You have access to the following tools:
# {tools}
 
# Tool names:
# {tool_names}
 
# Instructions:
# - You MAY think internally using Thought / Action / Observation
# - Use tools ONLY if required
# - When you are done, you MUST respond EXACTLY in this format:
 
# Final Answer:
# <only valid runnable Python code>
 
# Rules for Final Answer:
# - Python code only
# - No markdown
# - No explanations
# - No backticks
 
# User task:
# {input}
 
# {agent_scratchpad}
# """)
 
 
# agent = create_react_agent(
#     llm=llm,
#     tools=tools,
#     prompt=prompt,
# )
 
# agent_executor = AgentExecutor(
#     agent=agent,
#     tools=tools,
#     verbose=True,
#     handle_parsing_errors=True,
#     #max_iterations=2,          
#     # max_execution_time=20,  
# )
 
 
# user_input = st.text_area(
#     "Describe the Python program you want:",
#     height=160,
# )
 
# if st.button("Generate Python Code"):
#     try:
#         result = agent_executor.invoke({"input": user_input})
#         st.code(result["output"], language="python")
#     except Exception as e:
#         st.error(e)