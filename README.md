# Self-Improving Agent

자율 개선 에이전트 서비스입니다. 매일 자동으로 코드베이스를 분석하고, 개선 작업을 수행하며, Pull Request를 생성합니다.

## 개요

이 프로젝트는 GitHub 레포지토리를 지속적으로 개선하는 자율 에이전트입니다.
백로그에서 작업을 선택하고, 코드를 변경하며, PR을 자동으로 생성합니다.

## 주요 기능

- 백로그 기반 자동 작업 선택: 우선순위에 따라 오늘 할 작업을 자동으로 선택
- 코드 자동 개선: 리팩토링, 버그 수정, 기능 추가 등을 자율적으로 수행
- PR 자동 생성: 변경 이유와 내용을 설명하는 PR을 자동으로 생성
- 백로그 자동 업데이트: 코드 및 제품 관점에서 새로운 개선점을 자동으로 추가

## 시작하기

### 요구 사항

- Python 3.10+
- Git
- GitHub CLI (gh)

### 설치

    git clone https://github.com/LSJJOON/self-improving-agent.git
    cd self-improving-agent
    pip install -e .

### 사용법

    python -m agent run

## 프로젝트 구조

    self-improving-agent/
    ├── agent/          # 에이전트 핵심 로직
    │   └── __init__.py
    ├── tests/          # 단위 테스트
    │   └── __init__.py
    ├── docs/           # 문서
    ├── BACKLOG.md      # 작업 목록 (에이전트가 자동 관리)
    ├── DECISIONS.md    # 의사결정 기록 (에이전트가 자동 기록)
    └── README.md       # 이 파일

## 라이선스

MIT License
