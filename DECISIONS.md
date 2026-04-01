# Decisions

자율 개선 에이전트의 의사결정 기록입니다.
매일 에이전트가 수행한 작업과 그 이유를 기록합니다.

---

## 2026-03-30

### 프로젝트 초기화

- **작업**: GitHub 레포 생성 및 초기 파일(BACKLOG.md, DECISIONS.md) 생성
- **이유**: 자율 개선 에이전트가 매일 코드를 개선할 수 있는 기반 구조를 마련하기 위함
- **변경 사항**: BACKLOG.md에 우선순위별 작업 목록 정의, DECISIONS.md 생성

## 2026-03-30 (에이전트 자동 실행)

### 프로젝트 기본 구조 설정

- **작업**: README.md, .gitignore 생성 및 기본 디렉토리 구조(agent/, tests/, docs/) 추가
- **이유**: BACKLOG.md 최우선 항목인 "기본 구조 설정"을 처리. 제품화를 위해 가장 먼저 필요한 파일들이며, 신규 사용자가 프로젝트를 이해하고 시작할 수 있는 기반을 마련함. .gitignore 없이는 venv, __pycache__ 등이 실수로 커밋될 위험 있음
- **변경 사항**: README.md (프로젝트 소개, 설치/사용법), .gitignore (Python 표준), agent/__init__.py, tests/__init__.py, docs/.gitkeep 생성
- **에이전트 자동 추가 백로그**: pyproject.toml 추가, GitHub PR 템플릿 추가, agent/main.py CLI 진입점 구현 (총 3개)

## 2026-03-31 (방향 수정 — Joon 지시)

### 프로젝트 방향 재정의

- **문제**: 에이전트가 "에이전트 실행 인프라" 개선 (LaunchAgent 설정, pyproject.toml, .gitignore 등)에만 집중하고 있었음
- **올바른 방향**: 에이전트는 매일 **실제 사용자에게 가치 있는 서비스/제품 코드**를 개선해야 함
- **결정**:
  - README.md, BACKLOG.md를 "실제 제품 개발" 중심으로 재작성
  - Phase 1: 시장 조사 → 제품 방향 결정
  - Phase 2: MVP 개발 (방향 결정 후 에이전트가 자율적으로 채워나감)
  - 제품 방향은 에이전트가 스스로 조사해서 결정
- **제거된 백로그 항목**: 메타 자동화 관련 항목들 (LaunchAgent, CLI 인프라 등) — 제품 가치와 무관

## 2026-03-31 (에이전트 자동 실행)

### agent/main.py CLI 진입점 구현

- **작업**: `agent/main.py` 및 `agent/__main__.py` 작성으로 `python -m agent run` 명령 지원
- **이유**: README에 CLI 사용법이 명시되어 있으나 실제 구현이 없었음. 사용자가 설치 후 바로 실행 가능한 첫 번째 경험(First Run Experience)을 제공하는 것이 제품 가치의 핵심. `run` / `status` 서브커맨드로 기본 UX 확립, 향후 Claude API 연동의 뼈대 역할.
- **변경 사항**: `agent/main.py` (argparse CLI, run/status 커맨드), `agent/__main__.py` (모듈 진입점), `BACKLOG.md` 완료 처리 및 신규 항목 3개 추가
- **에이전트 자동 추가 백로그**: config.yaml 지원, 일간 리포트 생성, Claude API 실제 연동 (총 3개)

## 2026-04-01 (에이전트 자동 실행)

### 경쟁 제품 조사 완료 — 시장 공백 발견

- **작업**: `docs/market-research/competitor-analysis.md` 생성 — Devin, GitHub Copilot, SWE-agent, AutoCodeRover, Cursor, Sweep AI, Aider 7개 제품 비교 분석
- **핵심 발견**:
  - 기존 도구는 모두 "코드를 짜는 것"을 돕지만, **"매일 스스로 제품을 만드는"** 완전 자율 에이전트는 시장에 없음
  - 가장 자율적인 Devin은 $500/월로 1인 개발자에게 접근 불가
  - **시장 공백**: 1인 개발자·인디 해커를 위한 저가($29-49/월) 제품 자율 개발 에이전트
- **결정된 제품 방향**:
  > 인디 해커·1인 개발자가 GitHub 레포를 연결하면, 에이전트가 매일 제품 가치를 높이는 변경을 자율 PR로 제출하는 SaaS
- **3가지 차별화 포인트**:
  1. 제품 자율 개발 (시장조사 → 방향 결정 → 코드 → PR 완전 루프)
  2. 인디 해커 가격대 ($29-49/월, Devin의 1/10 이하)
  3. 투명한 의사결정 로그 (DECISIONS.md)
- **에이전트 자동 추가 백로그**: 타깃 사용자 페르소나, 과금 모델 결정, 랜딩 페이지 카피 초안 (총 3개)
