import os

from langchain_ollama import ChatOllama
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent

# os.environ["LANGSMITH_TRACING"] = "true"
# os.environ["LANGSMITH_API_KEY"] = ""

model = ChatOllama(model="qwen3:8b")
tools = [DuckDuckGoSearchRun()]
model_with_tools = model.bind_tools(tools)
agent = create_react_agent(model, tools)

result = agent.invoke(
    {"messages": [HumanMessage(content="Summarize any recent advancements in nuclear power")]}
)
for m in result["messages"]:
    m.pretty_print()
