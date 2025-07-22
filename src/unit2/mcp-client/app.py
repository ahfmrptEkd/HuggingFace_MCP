import gradio as gr
import os
from smolagents import InferenceClientModel, CodeAgent, MCPClient

mcp_client = None
try:
    mcp_client = MCPClient(
        {"url": "https://ahfmrptEkd-mcp-sentiment.hf.space/gradio_api/mcp/sse"}
    )
    tools = mcp_client.get_tools()

    # 스페이스에서는 HF_TOKEN이 자동으로 제공될 수도 있음
    model = InferenceClientModel(token=os.getenv("HF_TOKEN"))
    
    agent = CodeAgent(
        tools=[*tools], 
        model=model, 
        additional_authorized_imports=["json", "ast", "urllib", "base64"]
    )

    demo = gr.ChatInterface(
        fn=lambda message, history: str(agent.run(message)),
        type="messages",
        examples=["Analyze the sentiment of the following text: 'This is awesome'"],
        title="Agent with MCP Tools",
        description="This is a simple agent that uses MCP tools to answer questions.",
    )

    demo.launch()
    
except Exception as e:
    print(f"Error: {e}")
    demo = gr.ChatInterface(
        fn=lambda message, history: f"Setup Error: Please check space configuration. {str(e)}",
        type="messages",
        title="Agent Setup Error",
    )
    demo.launch()
    
finally:
    if mcp_client is not None:
        mcp_client.disconnect()