# tool prompt

I tried a bunch of different methods of defining and passing the tool to other models besides qwen3 to get any of them to use the
model properly. llama3.1:8b was close, but even when it figured out it needed to request the companies individually it would still
try to pass an array of the company names into the employee_info function. I tried setting the @tool anotation explicitly and adding
in annotations on the parameters, and I tried defining the interface using a pydantic BaseModel and attaching that to the annotation.
The only thing that seems to work for this version of llama at least is to give it an extra specific set of directions explicitly
about the tool as part of the prompt.

Unfortunately llama3.1:8b model tends to then do the math wrong anyway. But at least it calls the tool and collects the data it needs.
Here are some example traces, the link text is the command line I used to run the test and it links to a Langsmith trace of the 
execution:

* [python ./live_search.py llama3.1:8b](https://smith.langchain.com/public/7d86d7d6-3ba0-47b7-b02a-80c5538af122/r)
* [python ./live_search.py llama3.1:70b](https://smith.langchain.com/public/a721a486-0260-47d7-b5f6-bc9d7877d5e7/r)
* [python ./live_search.py](https://smith.langchain.com/public/80c36394-da85-4a8f-92f0-f705b61726bc/r)
