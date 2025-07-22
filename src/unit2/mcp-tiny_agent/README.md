# prerequisite
```
npm i mcp-remote

uv pip install "huggingface_hub[mcp]>=0.32.0"
```

# how to start
```
# agent.json
{
	"model": "Qwen/Qwen2.5-72B-Instruct",
	"provider": "nebius",
	"servers": [
		{
			"type": "stdio",
			"config": {
				"command": "npx",
				"args": [
					"mcp-remote", 
					"http://localhost:7860/gradio_api/mcp/sse"
				]
			}
		}
	]
}
```
```
tiny-agents run agent.json
```
**Ensure using "huggingface-cli login" to provide api to tiny-agent library.**


Here we have a basic Tiny Agent that can connect to our Gradio MCP server. It includes a model, provider, and a server configuration.

|Field| Dscription|
|---|---|
|model| The open source model to use for the agent |
|provider| The inference provider to use for the agent |
|servers| The servers to use for the agent. We’ll use the mcp-remote server for our Gradio MCP server. |


# if using running local model
```
{
	"model": "Qwen/Qwen3-32B",
	"endpointUrl": "http://localhost:1234/v1",
	"servers": [
		{
			"type": "stdio",
			"config": {
				"command": "npx",
				"args": [
					"mcp-remote",
					"http://localhost:1234/v1/mcp/sse"
				]
			}
		}
	]
}
```
Here we have a Tiny Agent that can connect to a local model. It includes a model, endpoint URL (http://localhost:1234/v1), and a server configuration. The endpoint should be an OpenAI-compatible endpoint.