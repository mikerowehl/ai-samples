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

* [qwen3:4b](https://smith.langchain.com/public/cf46fc11-92be-48cf-96e3-8487d47445a9/r) - pass
* [qwen3:8b](https://smith.langchain.com/public/a8876d3a-31e9-4e3a-90b3-8dbfbb2d17ce/r) - pass
* [qwen3:14b](https://smith.langchain.com/public/6e0da7dd-222d-4c7f-9bc3-e79e44076269/r) - pass
* [llama3.2:1b](https://smith.langchain.com/public/a54353f3-1583-45aa-9b59-5ad3f6f4e737/r) - fail
* [llama3.2:3b](https://smith.langchain.com/public/64e04e92-e08a-4d03-b8da-ff4e80f92f99/r) - fail
* [llama3.1:8b](https://smith.langchain.com/public/02b045de-816d-4b18-a7b9-4935dc1dab5d/r) - fail
* [mistral:7b](https://smith.langchain.com/public/d04ba61d-4a78-4830-ac1a-cc8536c2468d/r) - fail
* [deepseek-r1:1.5b](https://smith.langchain.com/public/1cdd7868-523f-494d-ada2-508685cec2ab/r) - fail
* [deepseek-r1:7b](https://smith.langchain.com/public/45487bc3-7eba-43dc-b5a9-8af0dea508cf/r) - fail
* [deepseek-r1:8b](https://smith.langchain.com/public/cc8306ed-b249-48dd-9fb7-11db3e5c2c48/r) - fail
* [deepseek-r1:14b](https://smith.langchain.com/public/c56cd7c2-7c9d-49bb-83fd-8eb621a08144/r) - fail

I had high hopes for the Deepseek models, but despite the ollama library saying they support tool
calling, the Langgraph react agent doesn't think it has what it needs. And the llama versions look like
they might be pretty close. But instead of calling the tool using the args provided it tried to call
using an array of strings. The way that tool shows up in langsmith is with an explicit type of string
on the company_name parameter. Maybe that's not how the tool gets presented to the LLM internally? I bet
if the tool was updated or if better tool signature info was passed to llama it would be able to get 
there.
