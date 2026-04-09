# 🚀 ShipCrew — 자는 동안 제품이 자란다

> AI 에이전트가 매일 당신의 제품을 개선하는 자율 코드 개발 SaaS

[![Deploy](https://img.shields.io/badge/Landing_Page-Live-brightgreen)](https://shipcrew.dev)
[![Phase](https://img.shields.io/badge/Phase-2_MVP_개발-blue)]()
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

## ShipCrew가 뭔가요?

GitHub 레포를 연결하면, AI 에이전트가 **매일 자동으로** 코드를 분석하고 제품 가치를 높이는 변경을 PR로 제출합니다.

- 🤖 **완전 자율 제품 개발** — 시장조사부터 코드 작성까지 에이전트가 스스로
- 📈 **매일 1 PR, 꾸준한 성장** — 자는 동안에도 제품이 개선됨
- 📋 **투명한 의사결정 로그** — 왜 그렇게 바꿨는지 항상 기록

## 누구를 위한 건가요?

**1인 개발자 · 인디 해커** — 시간은 부족하고 만들고 싶은 건 많은 당신.

> "혼자서 제품 만들고, 마케팅하고, 고객 지원까지 하다 보면 코드 개선은 늘 뒤로 밀려요. ShipCrew가 그 빈자리를 채워줍니다."

## 가격

| | Free | Pro | Team |
|---|---|---|---|
| **가격** | $0/월 | $29/월 | $79/월 |
| **레포** | 공개 1개 | 5개 | 무제한 |
| **실행 주기** | 주 1회 | 매일 | 매일 |
| **PR 제한** | 월 4개 | 무제한 | 무제한 |
| **Slack 알림** | ❌ | ✅ | ✅ |
| **팀원** | 1명 | 1명 | 5명 |

## 현재 개발 상태

📍 **Phase 2 — MVP 개발 진행 중** (2026-04-06 ~)

| 완료 | 진행중 |
|------|--------|
| ✅ 경쟁 제품 조사 (7개 분석) | 🔨 Vercel 배포 설정 |
| ✅ 타깃 사용자 정의 (인디 해커) | 🔨 Waitlist 이메일 수집 백엔드 |
| ✅ 과금 모델 설계 (Free/Pro/Team) | 🔨 GitHub OAuth 연동 |
| ✅ 랜딩 페이지 카피 & HTML | |
| ✅ MVP 기술 아키텍처 설계 | |

## 기술 스택

- **프론트엔드**: Next.js 14 + Tailwind CSS + shadcn/ui (Vercel 배포)
- **백엔드**: FastAPI Python (Railway 배포)
- **DB**: Supabase (PostgreSQL + Auth)
- **에이전트**: Python + Claude API + Celery 워커
- **랜딩 페이지**: 정적 HTML + Tailwind CSS CDN (즉시 배포)

## 프로젝트 구조

```
self-improving-agent/
├── frontend/          # 랜딩 페이지 (정적 HTML)
│   └── index.html     # ShipCrew 랜딩 페이지
├── agent/             # 에이전트 코어 (Python)
│   ├── main.py        # CLI 진입점
│   └── __main__.py    # 모듈 실행 지원
├── docs/
│   ├── market-research/  # Phase 1 시장조사 결과
│   └── technical/        # 기술 설계 문서
├── tests/             # 테스트
├── vercel.json        # Vercel 배포 설정
├── BACKLOG.md         # 작업 백로그
└── DECISIONS.md       # 의사결정 기록
```

## 의사결정 기록

모든 결정은 [DECISIONS.md](DECISIONS.md)에 기록됩니다. 에이전트가 왜 그런 선택을 했는지 투명하게 추적할 수 있습니다.

## 라이선스

MIT License
