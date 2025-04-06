# x64dbgmcp
Model Context Protocol for x64dbg

## Working Minimal Version
This plug-in currently only supports two functions from the x64dbgSDK which are:
1. DbgCmdExec
2. DbgIsActive

**This also only works for x64dbg, no x86dbg support is implemented as of now**
I want to add most of the functions provided by the sdk so dynamic analysis can be as easy as conversing with an LLM. Link to functions [here](https://help.x64dbg.com/en/latest/developers/functions/index.html)

Most of the HTTP server code was generated by Claude Sonnet 3.7 so if it is over-complicated to some, that is why. 

This is my first repo, so I realize I may have made some mistakes. Any advice or additional functionality is welcome.

<video src="./Showcase.mp4" controls title="Title" width="500"></video>
