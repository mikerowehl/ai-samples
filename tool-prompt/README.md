# tool prompt

I tried a bunch of different methods of defining and passing the tool to other models besides qwen3 to get any of them to use the
model properly. llama3.1:8b was close, but even when it figured out it needed to request the companies individually it would still
try to pass an array of the company names into the employee_info function. I tried setting the @tool anotation explicitly and adding
in annotations on the parameters, and I tried defining the interface using a pydantic BaseModel and attaching that to the annotation.
The only thing that seems to work for this version of llama at least is to give it an extra specific set of directions explicitly
about the tool as part of the prompt.
