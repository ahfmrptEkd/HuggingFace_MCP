# HuggingFace MCP 학습 프로젝트 (Unit 2 ~ 3)

Model Context Protocol (MCP)를 활용한 실무 개발 프로젝트 모음입니다. 이 프로젝트는 **HuggingFace의 공식 MCP 과정**을 기반으로 하여 MCP의 기본 개념부터 실제 적용까지 단계적으로 학습할 수 있도록 구성되었습니다.

![MCP Course Banner](https://github.com/user-attachments/assets/d26dcc5e-46cb-449e-aecb-49ece10d342a)

## 📚 프로젝트 개요

이 저장소는 MCP(Model Context Protocol)의 기본 개념부터 실무 적용까지 체계적으로 학습할 수 있는 완전한 교육 프로젝트입니다:

### 📖 이론 학습 (docs/)
- **Unit 1**: MCP 기본 개념, 통합 문제, 핵심 용어 이해
- **Unit 2**: Gradio 자원을 활용한 MCP 서버/클라이언트 구현 이론
- **Unit 3**: Claude Code 연동 및 실무 워크플로우 구축 가이드

### 🛠️ 실습 프로젝트 (src/)

#### Unit 2: 기본 MCP 구현
- **mcp-server**: TextBlob 기반 감정 분석 Gradio 서버
- **mcp-client**: HuggingFace.js 기반 MCP 클라이언트
- **mcp-tiny_agent**: SmolAgents 기반 통합 에이전트

#### Unit 3: 실무 워크플로우 구축  
- **모듈 1**: 기본 MCP 서버 구축 - PR 분석 및 템플릿 제안
- **모듈 2**: GitHub Actions 통합 - 웹훅 처리 및 CI/CD 자동화  
- **모듈 3**: Slack 알림 시스템 - 팀 커뮤니케이션 워크플로우

## 🏗️ 프로젝트 구조

```
HuggingFace_MCP/
├── docs/                      # 📖 학습 문서
│   ├── Unit1.md              # MCP 기본 개념 및 이론
│   ├── Unit2.md              # Gradio 기반 구현 가이드 
│   ├── Unit3.md              # Claude Code 워크플로우 
│   └── imgs/                 # 문서용 이미지 자료
│
├── src/
│   ├── unit2/                # 🛠️ 기본 MCP 구현
│   │   ├── mcp-server/       # Gradio 감정 분석 서버
│   │   │   ├── app.py        # TextBlob 기반 서버
│   │   │   └── requirements.txt
│   │   ├── mcp-client/       # HuggingFace.js 클라이언트
│   │   │   ├── app.py        # Gradio 인터페이스
│   │   │   └── requirements.txt
│   │   └── mcp-tiny_agent/   # SmolAgents 통합 에이전트
│   │       ├── agent.json    # 에이전트 설정
│   │       └── README.md
│   │
│   └── unit3/                # 🚀 실무 워크플로우 구축
│       ├── build-mcp-server/          # 모듈 1 - 기본 MCP 서버
│       │   └── starter/
│       │       ├── server.py          # PR 분석 및 템플릿 제안 도구
│       │       ├── test_server.py     # 단위 테스트
│       │       └── README.md
│       ├── github-actions-integration/ # 모듈 2 - GitHub Actions 통합
│       │   └── starter/
│       │       ├── server.py          # GitHub 웹훅 처리 도구
│       │       ├── webhook_server.py  # 웹훅 서버
│       │       ├── test_server.py     # 통합 테스트
│       │       └── README.md
│       ├── slack-notification/        # 모듈 3 - Slack 알림 시스템
│       │   └── starter/
│       │       ├── server.py          # Slack 알림 발송 도구
│       │       ├── webhook_server.py  # 웹훅 서버
│       │       ├── test_server.py     # 종단간 테스트
│       │       └── README.md
│       ├── team-guidelines/           # 팀 개발 가이드라인
│       │   ├── coding-standards.md    # 코딩 표준
│       │   └── pr-guidelines.md       # PR 작성 가이드라인
│       ├── templates/                 # PR 템플릿 모음
│       └── pyproject.toml            # 프로젝트 의존성 관리
│
└── README.md                
```

## 🚀 주요 기능

### Unit 2: 기본 MCP 구현
- **감정 분석 서버**: TextBlob 기반 Gradio MCP 서버 구축
- **다중 클라이언트 지원**: HuggingFace.js와 SmolAgents 연동
- **Hugging Face Spaces 배포**: 원격 MCP 서버 배포 및 연결
- **크로스 플랫폼 통합**: 다양한 클라이언트에서 동일한 서버 활용

### Unit 3: 실무 워크플로우 구축

#### 모듈 1: 기본 MCP 서버
- **파일 변경사항 분석**: Git diff 정보를 통한 코드 변경 분석
- **PR 템플릿 관리**: 다양한 템플릿 제공 및 추천 시스템
- **인텔리전트 제안**: Claude AI를 활용한 최적 템플릿 추천

#### 모듈 2: GitHub Actions 통합
- **웹훅 처리**: GitHub 이벤트 실시간 수신 및 처리
- **CI/CD 자동화**: 빌드 실패/성공 알림 자동화
- **MCP 프롬프트**: 표준화된 CI/CD 워크플로우 구축

#### 모듈 3: Slack 알림 시스템
- **실시간 알림**: CI/CD 결과를 Slack으로 즉시 전송
- **포맷된 메시지**: 실패/성공 상황별 맞춤형 메시지 포맷
- **종단간 통합**: GitHub → MCP → Slack 완전 자동화

## 🛠️ 기술 스택

### 핵심 프레임워크
- **Python 3.11+**: 메인 프로그래밍 언어
- **MCP SDK**: Model Context Protocol 구현
- **Gradio**: 웹 기반 MCP 서버/클라이언트 인터페이스

### 데이터 처리 및 분석
- **TextBlob**: 자연어 처리 및 감정 분석
- **Git**: 코드 변경사항 분석
- **JSON**: 구조화된 데이터 교환

### 개발 도구 및 배포
- **uv**: 고성능 Python 패키지 관리자
- **pytest**: 테스트 프레임워크
- **Hugging Face Spaces**: 원격 서버 배포

### 외부 API 통합
- **Slack API**: 팀 커뮤니케이션 통합
- **GitHub API**: 소스 코드 관리 통합
- **Cloudflare Tunnel**: 로컬 서버 외부 노출

### 클라이언트 라이브러리
- **HuggingFace.js**: JavaScript 기반 MCP 클라이언트
- **SmolAgents**: Python 기반 에이전트 프레임워크
- **mcp-remote**: 원격 MCP 서버 연결 도구

## 📋 전제 조건

- Python 3.11 이상
- [uv 패키지 매니저](https://docs.astral.sh/uv/getting-started/installation/) 설치
- Git 기본 지식
- GitHub 계정 및 저장소
- Slack 워크스페이스 (모듈 3용)

## 🚀 빠른 시작

### 1. 환경 설정

```bash
# 저장소 클론
git clone https://github.com/ahfmrptEkd/HuggingFace_MCP.git
cd HuggingFace_MCP/src/unit3

# 의존성 설치
uv sync

# 가상환경 활성화
source .venv/bin/activate
```

### 2. 프로젝트별 실행

각 프로젝트는 독립적으로 실행할 수 있습니다:

```bash
# Unit 2: 기본 MCP 구현
# 1. 감정 분석 서버 (Gradio)
cd src/unit2/mcp-server
pip install -r requirements.txt
python app.py

# 2. MCP 클라이언트 (Gradio)  
cd src/unit2/mcp-client
pip install -r requirements.txt
python app.py

# 3. Tiny Agent 실행
cd src/unit2/mcp-tiny_agent
npm i mcp-remote
uv pip install "huggingface_hub[mcp]>=0.32.0"
tiny-agents run agent.json

# Unit 3: 실무 워크플로우 구축
# 모듈 1: 기본 MCP 서버
cd src/unit3/build-mcp-server/starter
uv sync
uv run server.py

# 모듈 2: GitHub Actions 통합
cd src/unit3/github-actions-integration/starter
uv sync
python webhook_server.py  # 별도 터미널
uv run server.py

# 모듈 3: Slack 알림 시스템
cd src/unit3/slack-notification/starter
uv sync
export SLACK_WEBHOOK_URL="your-webhook-url" or .env 안에 "your-webhook-url" 설정하기
uv run server.py
```

### 3. Claude Code와 연동

```bash
# Unit 3 MCP 서버 등록 (절대 경로 사용)
claude mcp add [mcp 이름] -- uv --directory /absolute/path/to/src/unit3/build-mcp-server/starter run server.py

# Unit 2 Gradio 서버 연결 (mcp-remote 사용)
# 먼저 Gradio 서버 실행 후
cd src/unit2/mcp-server && python app.py

# 별도 터미널에서 mcp-remote로 연결
npx mcp-remote http://localhost:7860/gradio_api/mcp/sse

# 등록 확인
claude mcp list
```

## 🧪 테스트 실행

### Unit 2: 기본 MCP 구현 테스트
```bash
# Gradio 서버 테스트 (브라우저에서 수동 테스트)
cd src/unit2/mcp-server
python app.py
# http://localhost:7860 에서 감정 분석 테스트

# Tiny Agent 테스트
cd src/unit2/mcp-tiny_agent
tiny-agents run agent.json
# "Analyze the sentiment of 'I love programming!'" 입력하여 테스트
```

### Unit 3: 실무 워크플로우 테스트
```bash
# 전체 테스트 실행
cd src/unit3
uv run pytest test_server.py -v

# 특정 모듈 테스트
cd src/unit3/slack-notification/starter
uv run pytest test_server.py::test_send_slack_notification -v

# MCP 서버 연결 테스트
cd src/unit3/build-mcp-server/starter
uv run pytest test_server.py::test_analyze_file_changes -v
```

## 📖 학습 과정

### 📚 이론 학습 과정 (docs/)

#### Unit 1: MCP 기본 개념 
- MCP 정의 및 "AI를 위한 USB-C" 개념 이해
- M×N 통합 문제와 MCP의 해결책
- 핵심 용어 및 프로토콜 구조 학습

#### Unit 2: Gradio 기반 구현 이론   
- Gradio를 활용한 MCP 서버/클라이언트 아키텍처
- TextBlob 기반 감정 분석 도구 설계
- Hugging Face Spaces 배포 전략

#### Unit 3: 실무 워크플로우 가이드
- Claude Code 연동 및 PR Agent 개념
- GitHub Actions 통합 패턴
- 실제 팀 환경에서의 MCP 활용법

### 🛠️ 실습 학습 과정 (src/)

#### 단계 1: 기본 MCP 구현 (Unit 2)
- Gradio 기반 감정 분석 MCP 서버 구축
- HuggingFace.js와 SmolAgents 클라이언트 연동
- 원격 서버 배포 및 다중 클라이언트 테스트

#### 단계 2: MCP 기본 개념 실습 (Unit 3 모듈 1)
- MCP 프로토콜의 핵심 원리 구현
- 도구(Tools)와 프롬프트(Prompts) 개발
- Claude Code와의 통합 패턴

#### 단계 3: 실무 통합 패턴 (Unit 3 모듈 2)
- GitHub Actions와의 연동 방법
- 웹훅 처리 및 이벤트 기반 아키텍처
- CI/CD 자동화 워크플로우 구축

#### 단계 4: 종단간 자동화 (Unit 3 모듈 3)
- Slack 통합을 통한 완전 자동화
- 실제 팀 워크플로우에 적용
- 프로덕션 레벨 MCP 서버 완성

## 🤝 기여 가이드라인

이 프로젝트는 학습 목적으로 제작되었습니다. 기여를 원하시면:

1. 이슈를 먼저 등록해 주세요
2. 포크 후 기능 브랜치를 생성하세요
3. 코딩 표준을 준수해 주세요 (`team-guidelines/coding-standards.md` 참조)
4. PR 가이드라인을 따라주세요 (`team-guidelines/pr-guidelines.md` 참조)

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

**원본 코스**: [HuggingFace MCP Course](https://github.com/huggingface/mcp-course)

## 🆘 문제 해결

### 자주 발생하는 문제

1. **MCP 서버 연결 실패**
   ```bash
   # 포트 충돌 확인
   lsof -i :8080
   ```

2. **Slack 웹훅 오류**
   ```bash
   # 환경변수 확인
   echo $SLACK_WEBHOOK_URL
   ```

3. **GitHub 웹훅 수신 실패**
   ```bash
   # Cloudflare 터널 상태 확인
   cloudflared tunnel --url http://localhost:8080
   ```

### 지원

- 📧 이슈 등록: [GitHub Issues](https://github.com/ahfmrptEkd/HuggingFace_MCP/issues)
- 💬 토론: [GitHub Discussions](https://github.com/ahfmrptEkd/HuggingFace_MCP/discussions)
- 📖 원본 과정: [HuggingFace MCP Course](https://github.com/huggingface/mcp-course)

---

⭐ **이 프로젝트가 도움이 되셨다면 스타를 눌러주세요!** ⭐

*MCP를 활용한 AI 기반 개발 워크플로우의 새로운 패러다임을 경험해보세요.*
