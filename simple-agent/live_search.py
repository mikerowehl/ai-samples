from langgraph.prebuilt import create_react_agent
import os

# os.environ["LANGSMITH_TRACING"] = "true"
# os.environ["LANGSMITH_API_KEY"] = ""

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

graph = create_react_agent(
    # "anthropic:claude-3-7-sonnet-latest",
    "ollama:qwen3:8b",
    tools=[employee_info],
    prompt="The current date is June 30, 2025. You are a helpful assistant. Use any tools provided to answer questions.",
)
inputs = {"messages": [{"role": "user", "content": "What was the combined headcount of the FAANG companies in 2024?"}]}
for chunk in graph.stream(inputs, stream_mode="updates"):
    print(chunk)
