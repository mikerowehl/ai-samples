# Multi-agent Supervisor (updates included below)

I have a few things I've done using tool/MCP hookups to LLM models. Generally
those have been working fantastic through langchain or with the ReACT agent
defaults in langgraph. I wanted to try out some more complicated flows, and I
had seen a few mentions of the supervisor models prebuilt in langgraph. In
theory they sound great. And I've seen some youtube videos saying they use the
supervisor framework. But my attempts to run even the basic samples using
anything besides the openai models has just failed completely. I've seen other
people show off their tools where they say they use qwen3 with the supervisor
agent, but I can't get it to run at all.

I'm just recording my test here so I can come back in a bit and try this again
in case I hit some weird quirk in updates. What I'm trying to get working is 
the first basic example of using a supervisor agent from the docs:
[https://github.com/langchain-ai/langgraph-supervisor-py](https://github.com/langchain-ai/langgraph-supervisor-py)

My version is in [supervisor_sample.py](supervisor_sample.py)
and the only thing I've changed is
moving the model underlying the agents from gpt-4o to qwen3:8b (running
locally using ollama).
I haven't been able to get this to make it past the first handoff
from the supervisor at all. It seems like the model has everyting it needs to
determine it needs to make a tool call to pass control, but it just never
actually outputs the call to the tool:

```
================================ Human Message =================================

what's the combined headcount of the FAANG companies in 2024?
================================== Ai Message ==================================
Name: supervisor

<think>
Okay, the user is asking for the combined headcount of FAANG companies in 2024. First, I need to recall which companies are considered FAANG. FAANG typically stands for Facebook (now Meta), Amazon, Apple, and Netflix. Wait, sometimes Google is included too, but the user specified FAANG, so probably just the four.

Next, I need the latest headcount data for each of these companies as of 2024. Since the user is asking for 2024 data, I should check if there are recent reports or press releases from these companies. However, I don't have real-time data access. The research expert would be the right person to consult here because they can look up the most recent information from reliable sources like company reports, news articles, or official announcements.

I should transfer the query to the research_expert to gather the necessary data from each company and sum them up. The math expert might be needed later to add the numbers, but first, I need the individual figures. So, the correct tool to use here is transfer_to_research_expert.
</think>
```

It works fine if I swap it to the gpt model, but it just doesn't want to make
tool calls as the supervisor agent. I figured maybe something was just broken
with the latest snapshot of the model, or maybe there was something in the
tooling that was injecting something that was keeping the model from actually
calling the tools. But I turned on langsmith and I can't see anything in the
guts of the calls that would make it fail to actually operate.

I tried going back to the simpler model just to make sure, and made the
simpler react agent using qwen3 and a call out to a web search, which I have
in [tool_use.py](tool_use.py). That runs with all the current most recent
versions of the model itself and the libraries, calls the tool and does
everything as expected. I assume there's something in the depths of the
supervisor harness for langgraph that's keeping it from even trying. My
assumption was that the models besides gpt might not work very well in the
framework, especially if they're not tuned for reasoning. But having it fail
outright and just not hook up to the handoffs feels pretty weird.

## Update June 28, 2025
With ollama updated to the latest from their installer (0.9.3) and updating
the versions of the langchain/graph libraries to the latest this
at least passes control around now. qwen3 thinks it's 2023 however and tries
to estimate the values based on best guesses instead of actually calling any 
tools. But maybe some updating the prompt will get it to display the intended
behavior.

But also, the examples from Langchains
[Agents from Scratch](https://github.com/langchain-ai/agents-from-scratch)
example that goes along with one of their recent tutorial series works very
well with the local models I've tested. Maybe this supervisor library is a
bit too bleeding edge and the better method is to build the graph manually.
