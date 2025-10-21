# 🤖 HuggingFace MCP 학습 및 실무 워크플로우 구축 프로젝트

> HuggingFace MCP 공식 과정을 기반으로 MCP 서버/클라이언트 구현부터 GitHub Actions 및 Slack을 연동한 실무 PR 자동화 워크플로우 구축까지

![MCP Course Banner](https://github.com/user-attachments/assets/d26dcc5e-46cb-449e-aecb-49ece10d342a)

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![MCP](https://img.shields.io/badge/MCP-server--python-green.svg)
![Gradio](https://img.shields.io/badge/gradio-latest-orange.svg)

*본 프로젝트는 HuggingFace MCP 공식 과정을 기반으로 합니다.*

---
<br>

## 🎯 프로젝트 개요: 30초 요약 (STAR)

* **S (Situation / 문제)**
  
  AI 모델과 외부 도구/데이터 소스를 연동하는 것은 M x N 통합 문제로 인해 복잡하고 비효율적입니다. 개발자는 AI 모델이 git 변경사항 분석, CI/CD 상태 모니터링, 팀 알림 발송 등 실제 개발 워크플로우와 원활하게 상호작용할 수 있는 표준화된 방법이 필요했습니다.

* **T (Task / 목표)**
  
  HuggingFace의 MCP(Model Context Protocol) 과정을 통해 MCP의 기본 개념을 학습하고, 이를 실제 개발 워크플로우에 적용하는 **PR 에이전트(PR Agent)**를 구축하는 것이 목표였습니다. 구체적으로는 **PR 템플릿 추천**, **GitHub Actions 모니터링**, **Slack 알림 자동화** 기능을 구현하고자 했습니다.

* **A (Action / 해결)**

  1. **Unit 2 (기본 구현)**: Gradio를 활용하여 TextBlob 기반 감정 분석 MCP 서버와 HuggingFace.js/SmolAgents 클라이언트를 구현하고 Hugging Face Spaces에 배포했습니다.

  2. **Unit 3 (실무 워크플로우)**: `FastMCP`를 사용하여 PR 에이전트 서버를 구축했습니다.
     * **Module 1**: `git diff` 분석 및 PR 템플릿 추천 도구 (`analyze_file_changes`, `get_pr_templates`, `suggest_template`) 구현.
     * **Module 2**: GitHub Actions 웹훅을 처리하고(`webhook_server.py`), CI/CD 상태를 모니터링하는 도구(`get_recent_actions_events`, `get_workflow_status`) 및 관련 프롬프트(`analyze_ci_results` 등) 구현. Cloudflare Tunnel을 이용한 로컬 테스트 환경 구축.
     * **Module 3**: CI/CD 결과를 Slack으로 자동 알림하는 도구(`send_slack_notification`) 및 서식 프롬프트(`format_ci_failure_alert` 등) 구현.

* **R (Result / 결과)**
  
  * **핵심 산출물**: Git 변경사항 분석, GitHub Actions 모니터링, Slack 알림 기능을 갖춘 **완전한 PR 에이전트 MCP 서버**를 성공적으로 구축했습니다.
  * **기술적 성과**: MCP의 핵심 요소인 **Tools**와 **Prompts**를 모두 활용하여 복잡한 개발 워크플로우를 자동화하는 시스템을 구현했습니다. `uv`를 통한 효율적인 패키지 관리 및 `pytest`를 활용한 테스트 코드를 작성했습니다.

---
<br>

## 🛠️ 기술적 구현 (Action): 핵심 의사결정

이 프로젝트는 MCP 개념을 실제 개발 워크플로우에 적용하는 과정에 중점을 둡니다.

### 1. Unit 2: MCP 기본 개념 학습 및 구현

* **Gradio 기반 MCP 서버/클라이언트**: Gradio의 내장 MCP 지원을 활용하여 신속하게 웹 기반 서버(`mcp-server/app.py`)와 클라이언트(`mcp-client/app.py`)를 구축했습니다. 이를 통해 MCP 통신 흐름과 기본 구조를 학습했습니다.
  * **Tool**: TextBlob을 이용한 감정 분석 기능을 MCP Tool로 노출.
* **다양한 클라이언트 연동**: 동일한 Gradio 서버에 HuggingFace.js 기반 웹 클라이언트와 Python 기반 SmolAgents(`mcp-tiny_agent/agent.json`)를 연동하여 MCP의 상호 운용성을 확인했습니다.
* **Hugging Face Spaces 배포**: 개발된 Gradio 서버를 Spaces에 배포하여 원격 MCP 서버 운영 경험을 쌓았습니다.

### 2. Unit 3: 실무 워크플로우 자동화 (PR 에이전트)

* **FastMCP 서버 채택**: Unit 3에서는 Gradio 대신 Python 기반의 `FastMCP` 라이브러리를 사용하여 보다 세밀한 제어가 가능한 독립형 MCP 서버를 구축했습니다 (`unit3/.../server.py`).

* **Module 1 (PR 생성 보조)**:
  * **`analyze_file_changes` Tool**: `subprocess`를 사용하여 `git diff` 명령어를 실행하고, 변경된 파일 목록, 통계, diff 내용을 JSON 형식으로 반환합니다. 대규모 diff 출력을 제어하기 위해 `max_diff_lines` 매개변수를 추가했습니다.
  * **`get_pr_templates` / `suggest_template` Tools**: 로컬 `templates/` 디렉토리에서 PR 템플릿을 로드하고, 사용자가 제공한 변경 유형(`change_type`)에 기반하여 가장 적합한 템플릿을 추천하는 로직을 구현했습니다. 이는 AI가 판단할 수 있도록 원시 데이터(템플릿 목록, 변경 요약)를 제공하는 MCP 철학을 따릅니다.

* **Module 2 (CI/CD 모니터링)**:
  * **Webhook 처리**: 별도의 `aiohttp` 기반 웹훅 서버(`webhook_server.py`)를 구축하여 GitHub Actions 이벤트를 수신하고, 이를 `github_events.json` 파일에 저장합니다. 이는 MCP 서버와 비동기적으로 작동합니다.
  * **`get_recent_actions_events` / `get_workflow_status` Tools**: `github_events.json` 파일을 읽어 최근 CI/CD 이벤트나 특정 워크플로우의 최신 상태를 조회하는 기능을 구현했습니다.
  * **MCP Prompts 도입**: `@mcp.prompt()` 데코레이터를 사용하여 `analyze_ci_results`, `troubleshoot_workflow_failure` 등 표준화된 분석 워크플로우를 정의했습니다. 이는 Claude Code와 같은 클라이언트 AI에게 특정 작업을 수행하도록 지시하는 가이드 역할을 합니다.

* **Module 3 (팀 커뮤니케이션)**:
  * **`send_slack_notification` Tool**: `requests` 라이브러리를 사용하여 Slack Incoming Webhook URL (`SLACK_WEBHOOK_URL` 환경 변수)로 메시지를 전송하는 기능을 구현했습니다. Slack 마크다운을 지원합니다.
  * **서식 Prompts**: `format_ci_failure_alert`, `format_ci_success_summary` 등 Slack 메시지 서식을 정의하는 프롬프트를 추가했습니다. 이는 AI가 CI/CD 결과를 기반으로 일관된 형식의 알림을 생성하도록 유도합니다.
  * **End-to-End Workflow**: GitHub 이벤트 발생 → Webhook 서버 수신 → MCP 서버의 Tools/Prompts 호출 (Claude Code 경유) → Slack 알림 발송으로 이어지는 완전 자동화 워크플로우를 완성했습니다.

---
<br>

## 📊 결과 및 성과 (Result)

* **MCP 과정 이수**: HuggingFace MCP 과정의 Unit 1(이론), Unit 2(기본 구현), Unit 3(실무 응용) 학습 목표 달성.
* **실용적 MCP 서버 구현**: 실제 개발 환경에서 유용하게 사용될 수 있는 PR 관리 및 CI/CD 모니터링 자동화 워크플로우를 MCP 서버로 구현했습니다.
* **Tools와 Prompts 통합**: MCP의 핵심 기능인 Tools(기능 실행)와 Prompts(워크플로우 가이드)를 효과적으로 조합하여 사용하는 방법을 시연했습니다.
* **테스트 및 문서화**: 각 모듈별 테스트 코드(`test_server.py`)와 수동 테스트 가이드(`manual_test.md`)를 작성하여 코드의 신뢰성과 재현성을 확보했습니다.

---
<br>

## 💡 주요 학습 포인트 (Learnings)

* **MCP의 가치**: M x N 통합 문제를 해결하고 AI 모델과 외부 시스템 간의 상호 운용성을 높이는 MCP의 중요성을 실제 구현을 통해 이해했습니다.
* **MCP 서버 설계**: `FastMCP`를 사용하여 Tools와 Prompts를 정의하고, 비동기 처리를 통해 효율적인 서버를 구축하는 방법을 학습했습니다.
* **AI와의 협업**: 복잡한 로직을 직접 구현하기보다, AI(Claude Code 등)가 판단하고 작업을 수행할 수 있도록 적절한 데이터와 가이드(Prompts)를 제공하는 방식의 유연성과 강력함을 경험했습니다.
* **워크플로우 자동화**: Webhook, MCP 서버, 외부 API(Slack)를 연동하여 실제 개발 프로세스를 자동화하는 시스템 아키텍처 설계 및 구현 능력을 향상시켰습니다.

---
<br>

## 🚀 기술 스택

| 구분 | 기술 | 설명 |
|:-----|:-----|:-----|
| **MCP** | `mcp-server-python` (`FastMCP`), Gradio MCP | MCP 서버 구현 라이브러리 |
| **언어** | Python 3.11+ | 메인 프로그래밍 언어 |
| **웹 프레임워크** | Gradio (Unit 2), `aiohttp` (Unit 3 Webhook) | 웹 인터페이스 및 웹훅 서버 구축 |
| **패키지 관리** | `uv` | Python 패키지 설치 및 환경 관리 |
| **테스팅** | `pytest`, `pytest-asyncio` | 단위 및 통합 테스트 |
| **API 연동** | `requests` (Slack), `subprocess` (Git) | 외부 API 및 로컬 명령어 실행 |
| **NLP (Unit 2)** | `textblob` | 감정 분석 라이브러리 |
| **인프라 (선택)** | Hugging Face Spaces (Unit 2 배포), Cloudflare Tunnel (Unit 3 로컬 테스트) | 서버 배포 및 로컬 개발 환경 외부 노출 |
| **클라이언트** | HuggingFace.js (Unit 2), SmolAgents (Unit 2), Claude Code (Unit 3), `mcp-remote` (원격 서버 프록시) | MCP 서버와 상호작용하는 다양한 클라이언트 |

*기술 스택은 `src/unit3/pyproject.toml`, `src/unit2/.../requirements.txt` 파일에서 확인 가능합니다.*

---
<br>

## 🚀 시작하기 (Getting Started)

### 전제 조건

* Python 3.11 이상
* [uv 패키지 매니저](https://docs.astral.sh/uv/getting-started/installation/) 설치
* Git 기본 지식
* (Unit 3) GitHub 계정 및 저장소
* (Unit 3 Module 3) Slack 워크스페이스 및 Incoming Webhook URL
* (Unit 3) Claude Code (또는 다른 MCP 클라이언트)
<br>

### 1. 환경 설정 (Unit 3 기준)

```bash
# 저장소 클론
git clone https://github.com/ahfmrptekd/HuggingFace_MCP.git
cd HuggingFace_MCP/src/unit3

# 의존성 설치 (개발/테스트 도구 포함)
uv sync --all-extras

# 가상환경 활성화 (uv sync 시 자동으로 생성됨)
source .venv/bin/activate
```
<br>

### 2. 환경 변수 설정 (Unit 3 Module 3)

`src/unit3/slack-notification/starter/` 디렉토리에 `.env` 파일을 생성하고 Slack Webhook URL을 설정합니다. ([`.env.example`](.env.example) 참조)

```bash
# src/unit3/slack-notification/starter/.env
SLACK_WEBHOOK_URL="https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
```
<br>

### 3. 프로젝트별 실행

각 모듈의 서버는 독립적으로 실행할 수 있습니다. (Unit 3 기준)

```bash
# Module 1: 기본 MCP 서버
cd src/unit3/build-mcp-server/starter
uv run server.py

# Module 2: GitHub Actions 통합
cd src/unit3/github-actions-integration/starter
# 터미널 1: Webhook 서버 실행
python webhook_server.py
# 터미널 2: MCP 서버 실행
uv run server.py
# 터미널 3 (선택): Cloudflare Tunnel 실행 (GitHub Webhook 연동 시)
# cloudflared tunnel --url http://localhost:8080

# Module 3: Slack 알림 시스템
cd src/unit3/slack-notification/starter
# 터미널 1: Webhook 서버 실행
python webhook_server.py
# 터미널 2: MCP 서버 실행 (SLACK_WEBHOOK_URL 환경 변수 필요)
uv run server.py
```
<br>

### 4. Claude Code와 연동 (Unit 3 서버)

Claude Code 설정에서 MCP 서버를 등록합니다. **`cwd` (Current Working Directory) 경로를 실제 프로젝트 경로로 변경해야 합니다.**

```json
// Claude Code Settings (settings.json)
{
  "mcpServers": {
    "pr-agent-slack": { // MCP 서버 이름 (임의 지정 가능)
      "command": "uv",
      "args": ["run", "server.py"],
      // !!! 아래 cwd 경로를 실제 프로젝트의 Module 3 서버 경로로 수정하세요 !!!
      "cwd": "/absolute/path/to/HuggingFace_MCP/src/unit3/slack-notification/starter"
    }
  }
}
```

Claude Code를 재시작하면 서버가 연결됩니다.

---
<br>

## 🧪 테스트 실행 (Unit 3 기준)

각 모듈 디렉토리 내에서 `pytest`를 사용하여 테스트를 실행할 수 있습니다.

```bash
# 특정 모듈의 테스트 실행 (예: Module 3)
cd src/unit3/slack-notification/starter
uv run pytest test_server.py -v
```

수동 테스트 및 End-to-End 테스트는 각 모듈의 `manual_test.md` 파일을 참조하세요.

---
<br>

## 📁 프로젝트 구조

```
├── README.md
├── src/
│   ├── unit2/                           # MCP 기본 개념 학습
│   │   ├── mcp-server/                  # Gradio 기반 MCP 서버
│   │   ├── mcp-client/                  # Gradio 기반 MCP 클라이언트
│   │   └── mcp-tiny_agent/              # SmolAgents 클라이언트
│   └── unit3/                           # 실무 워크플로우 구현
│       ├── build-mcp-server/            # Module 1: PR 템플릿 추천
│       │   └── starter/
│       │       ├── server.py
│       │       └── templates/
│       ├── github-actions-integration/  # Module 2: CI/CD 모니터링
│       │   └── starter/
│       │       ├── server.py
│       │       └── webhook_server.py
│       └── slack-notification/          # Module 3: Slack 알림
│           └── starter/
│               ├── server.py
│               ├── webhook_server.py
│               └── test_server.py
└── docs/                                # 문서 및 가이드
```

---
<br>

## 📄 라이선스

이 프로젝트는 원본 HuggingFace MCP 과정의 라이선스를 따릅니다. 자세한 내용은 [LICENSE](src/unit3/LICENSE) 파일을 참조하세요.

## 📚 인용 및 참고자료

이 프로젝트는 HuggingFace의 공식 Model Context Protocol 과정을 기반으로 합니다:

```bibtex
@misc{mcp-course,
  author = {Burtenshaw, Ben and Notov, Alex},
  title = {The Model Context Protocol Course},
  year = {2025},
  howpublished = {\url{https://github.com/huggingface/mcp-course}},
  note = {GitHub repository - Unit 3 Implementation},
}
```
---

## 🙏 감사의 말

이 프로젝트는 HuggingFace 팀이 제공한 훌륭한 [MCP Course](https://github.com/huggingface/mcp-course)를 기반으로 합니다.
