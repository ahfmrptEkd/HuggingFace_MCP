# Unit2

---

---

이 유닛에서는 MCP 밑바닥에서부터 그라디오를 이용해서 구현합니다. 

# What you will learn

- Create an MCP Server using Gradio’s built-in MCP support
- Build a sentiment analysis tool that can be used by AI models
- Connect to the server using different client implementations:
    - A HuggingFace.js-based client
    - A SmolAgents-based client for Python
- Deploy your MCP Server to Hugging Face Spaces
- Test and debug the complete system

## Server side

- 그라디오를 이용해서 user interface를 구현한다. (`gr.Interface` )
- TextBlob을 이용해서 sentiment analysis 도구를 구현한다.
- HTTP와 MCP protocol를 이용해서 노출한다.

## Client side

- HuggingFace.js client를 구현한다.
- 또는 smolagents Python 클라이언트를 구현한다.
- 다른 클라이언트가 같은 서버를 쓰는것을 보여준다.

## Depolyment

- Hugging face spaces를 이용해서 서버를 배포한다.
- 클라이언트를 설정하고, 서버와 함께 작동한다.

---

# Using MCP clients with your application

만든 semantic analysis mcp application configure 예시

```python
{
  "mcpServers": {
    "sentiment-analysis": {
      "command": "npx",
      "args": [
        "-y", 
        "mcp-remote", 
        "https://YOURUSENAME-mcp-sentiment.hf.space/gradio_api/mcp/sse", 
        "--transport", 
        "sse-only"
      ]
    }
  }
}
```

여기서 `mcp-remote` 인자를 쓰는 이유는 대부분의 cursor 같은 MCP client들이 오직 local servers들만 (stdio) 지원하기 때문이다. 그리고 아직 OAuth authentication 을 하는 원격 서버들을 지원하지 않기 때문이다.

- `mcp-remote` 도구가 이 문제를 해결하는 다리 역활을 한다:
    - Runs locally on your machine
    - Forwards requests from Cursor to the remote MCP server
    - Uses the familiar configuration file format

---

# Unit2 project summay

MCP를 이해하는 것부터 End-to-End application을 만들었다.

- Gradio를 이용한 Text analyze MCP server
- Gradio를 이용한 tool를 쓰는 client
- Tiny-agent를 이용한 도구와 상호 작용할 수 이는 작은 에이전트 구축

이런 방식의 흐름으로 구축한 에이전트는 아래에 것들을 할 수 있다:

- 여러 도구 공급자에 연결
- 사용 가능한 도구를 동적으로 검색
- 맞춤형 text analyze 분석 도구 사용
- 파일 시스템에 액세스 및 웹 브라우징 과 같은 다른 기능과 결합