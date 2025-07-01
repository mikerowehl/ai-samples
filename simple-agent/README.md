# Simple Agent

Since the supervisor example didn't work with any of the ollama models I tried, and in general the tool calls
didn't even look correct when running inside the supervisor module, I wanted to back up a level and just make
sure I could create a simple agent with qwen. So I started with the
[weather example](weather.py) which was the example on the langgraph version of the create_react_agent() docs.
Note that there's an older create_react_agent() that had been part of langchain, that had very different
examples. This version seemed to behave well, it called the tool expected and passed the args expected for the
query given.

Once the very basics were working I tried getting a version that handled the example from the supervisor demo
I have sitting in another directory here. The idea there was to divide the problem of looking up and summing
headcounts as a demo of dividing up a problem. When I tried running just the web search part using qwen none
of it worked as expected. So I just wanted to make a version that at least got that part right. My modified
version is what's in the [live_search.py](live_search) example in this directory. Here are a few
things I adjusted while getting the react agent to work with qwen:

* qwen is pretty insistent about what it thinks the current date is, which is generally somewhere around 2023
right now. That's when training cut off. The side effect of that is that even with a tool to lookup data,
if you ask it for the "employee counts as of 2024" the model assumes you're talking about the future. So it'll
estimate on it's own instead of calling the tool. I explicitly put the date into the prompt. This is a pretty
well known problem with qwen, so you can find plenty of discussion about it online.
* with or without the date fix in there, the example as given for the supervisor agent wasn't getting qwen to
call the tool to find what it wanted. It knew it had a tool, it knew it needed employee counts from some
companies, but a tool that can "Search the web for information" just wasn't leading qwen to the right set of
actions. So I changed to tool to be named employee_info instead and make the comment about what it does
specifically about looking up company info.
* also changed the return from the tool to only give the details for the specific company passed in, so that
it couldn't cheat and shortcut calls. I wanted every call explicitly to show up in the trace.

Obviously this added a lot of very strict and fragile connections. I'll probably fool with the prompts and 
setup somewhat to see if I can get that to be a little less structured. But I was happy to at least get
something that looked like it was doing a bit of reasoning out of qwen. It's supposed to be a great
reasoning model, but it was just tripping over the default setups meant for the more mainstream models.

I've also captured the runs using some different models using Langsmith. I've run these on my local Linux
desktop system without a GPU, so please note that the execution times are extremely long. That's not the
fault of the model, it's just cause I'm playing around with some of these tools.

* [qwen3:8b](https://smith.langchain.com/public/a8876d3a-31e9-4e3a-90b3-8dbfbb2d17ce/r)
