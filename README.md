# AI Samples

These are just some notes for myself. Either bits of code from something that I want to make sure I keep around but
doesn't currently have a home, or things I intend to check back on. In particular, I'm currently trying to run some
AI stuff, but my personal interest is in using some local models where I can. And I've been finding
that lots of the tools that "allow you to swap to any model" by just swapping the identifier don't actually run at
all if you swap to something other than what was initially used. Understandable, we're in the early days of
a new style of development. But I would  like to see the new tools, in particular open source tools, 
allow for a selection of models. So just trying to figure out a few places where this isn't working as expected
currently and maybe we can come up with something that makes it a bit easier to spot issues.

* [supervisor sample](supervisor) - the base example from the langgraph supervisor module
* [simple react agent](simple-agent) - take the web search part of the supervisor example and make it work with qwen
* [tool prompt](tool-prompt) - change the prompt to force models to use the tool correctly
