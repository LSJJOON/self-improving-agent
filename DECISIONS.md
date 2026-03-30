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
