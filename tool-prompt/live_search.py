from langchain_core.language_models import BaseLanguageModel
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
import sys

def employee_info(company_name: str, year: int) -> str:
    '''Searches the web for info about the company during the year provided and returns employee count.'''
    match company_name.lower():
        case "facebook" | "meta":
            return f"As of {year} there were 67,317 employees at {company_name}"
        case "apple":
            return f"There were 164,000 employees at {company_name} during {year}"
        case "amazon":
            return f"There were 1,551,000 employees at Amazon"
        case "netflix":
            return f"Netflix had 14000 employees"
        case "google" | "alphabet":
            return f"As of {year} there were 181,269 employees at {company_name}"
        case _:
            return f"Unable to find employee info for {company_name}"

def make_agent(model: BaseLanguageModel):
    graph = create_react_agent(
        model=model,
        tools=[employee_info],
        prompt="The current date is June 30, 2025. You are a helpful assistant. Use any tools provided to answer questions. It is important to note that the tool provided only takes a single company name as an argument, do not attempt to pass an array.",
    )
    return graph

# Set the LANGSMITH_TRACING environment variable to "true" and the
# LANGSMITH_API_KEY to the key provided to you by Langsmith if you want to
# capture the detais of a run. The README alongside this script has some info
# about runs of this test captured with a few different open models:
# https://github.com/mikerowehl/ai-samples/tree/main/simple-agent
if __name__ == "__main__":
    model = "qwen3:8b"
    temperature = 0.0
    if len(sys.argv) > 1:
        model = sys.argv[1]
    if len(sys.argv) > 2:
        temperature = float(sys.argv[2])
    llm = ChatOllama(model=model, temperature=temperature)
    graph = make_agent(llm)
    inputs = {"messages": [{"role": "user", "content": "What was the combined headcount of the FAANG companies in 2024?"}]}
    # for chunk in graph.stream(inputs, stream_mode="updates"):
    #    print(chunk)
    result = graph.invoke(inputs)
    for r in result["messages"]:
        r.pretty_print()
