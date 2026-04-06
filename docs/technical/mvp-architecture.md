# MVP 기술 아키텍처 설계

> 작성일: 2026-04-06
> 상태: Phase 2 착수를 위한 기술 결정

## 1. 제품 개요

**ShipCrew** (가칭) — GitHub 레포를 연결하면, AI 에이전트가 매일 제품 가치를 높이는 코드 변경을 자율 PR로 제출하는 SaaS.

### 타깃 사용자
- 1인 개발자 / 인디 해커
- 사이드 프로젝트를 유지·발전시킬 시간이 부족한 개발자

### 핵심 가치 제안
- "내가 자는 동안 제품이 개선된다"
- Devin($500/월) 대비 1/10 가격($29-49/월)
- 투명한 의사결정 로그

## 2. MVP 범위 (Phase 2 첫 번째 목표)

MVP는 **"하나의 레포에 대해 매일 1개의 개선 PR을 생성"** 하는 것에 집중한다.

### MVP에 포함
- GitHub OAuth 로그인
- 레포 1개 연결
- 일간 자동 실행 (코드 분석 → 작업 선정 → PR 생성)
- 실행 결과 대시보드 (PR 이력, 오늘의 작업)
- 이메일 알림 (일간 리포트)

### MVP에 미포함 (Phase 3 이후)
- 멀티 레포
- Slack 연동
- 사용자 설정 커스터마이징
- 팀 기능
- 결제 시스템 (MVP는 무료 베타)

## 3. 시스템 아키텍처

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│   사용자     │────▶│  웹 앱       │────▶│  API 서버       │
│  (브라우저)  │◀────│  (Next.js)   │◀────│  (FastAPI)      │
└─────────────┘     └──────────────┘     └────────┬────────┘
                                                   │
                                          ┌────────┴────────┐
                                          │                 │
                                   ┌──────▼──────┐  ┌──────▼──────┐
                                   │  에이전트    │  │  데이터베이스│
                                   │  워커        │  │  (Supabase) │
                                   │  (Celery)    │  │             │
                                   └──────┬──────┘  └─────────────┘
                                          │
                                   ┌──────▼──────┐
                                   │  GitHub API  │
                                   │  + Claude API│
                                   └─────────────┘
```

## 4. 기술 스택 결정

### 프론트엔드: Next.js 14 (App Router)
- **선택 이유**: 1인 개발자가 가장 빠르게 풀스택 구현 가능
- SSR/SSG로 SEO 대응 (랜딩 페이지 겸용)
- Vercel 무료 배포로 초기 비용 $0
- Tailwind CSS + shadcn/ui로 빠른 UI 구현

### 백엔드 API: FastAPI (Python)
- **선택 이유**: 에이전트 코어가 Python이므로 동일 언어로 통합
- 비동기 처리 우수 (GitHub API, Claude API 호출)
- 자동 API 문서 (Swagger) 내장
- 타입 힌트로 안정성 확보

### 에이전트 코어: Python + Claude API
- **선택 이유**: 기존 agent/ 코드 활용, Claude가 코드 이해·생성 최강
- 실행 흐름: 레포 클론 → 코드 분석 → 작업 결정 → 구현 → PR 생성
- 스케줄러: Celery + Redis (일간 크론 작업)

### 데이터베이스: Supabase (PostgreSQL)
- **선택 이유**: 인증(Auth) 내장, 실시간 구독, 무료 티어 넉넉
- 스키마: users, repos, agent_runs, pull_requests 테이블
- Row Level Security로 멀티테넌트 보안

### 인프라/배포
- **프론트엔드**: Vercel (무료)
- **백엔드**: Railway 또는 Render ($5-7/월)
- **워커**: Railway (백엔드와 같은 플랫폼)
- **Redis**: Upstash (무료 티어)

### 예상 월 운영 비용 (MVP)
| 항목 | 비용 |
|------|------|
| Vercel (프론트) | $0 |
| Railway (백엔드+워커) | $5-10 |
| Supabase (DB) | $0 |
| Upstash Redis | $0 |
| Claude API (10명 베타) | ~$50-100 |
| GitHub API | $0 |
| **합계** | **~$55-110/월** |

## 5. 데이터 모델 초안

```sql
-- 사용자
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  github_id BIGINT UNIQUE NOT NULL,
  github_login TEXT NOT NULL,
  email TEXT,
  plan TEXT DEFAULT 'free',
  created_at TIMESTAMPTZ DEFAULT now()
);

-- 연결된 레포
CREATE TABLE repos (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id),
  github_repo_full_name TEXT NOT NULL,  -- "owner/repo"
  github_repo_id BIGINT NOT NULL,
  is_active BOOLEAN DEFAULT true,
  agent_config JSONB DEFAULT '{}',
  created_at TIMESTAMPTZ DEFAULT now()
);

-- 에이전트 실행 기록
CREATE TABLE agent_runs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  repo_id UUID REFERENCES repos(id),
  status TEXT NOT NULL,  -- 'pending', 'running', 'completed', 'failed'
  task_description TEXT,
  pr_url TEXT,
  pr_number INTEGER,
  started_at TIMESTAMPTZ,
  completed_at TIMESTAMPTZ,
  log JSONB DEFAULT '[]',
  created_at TIMESTAMPTZ DEFAULT now()
);
```

## 6. MVP 개발 로드맵 (Phase 2)

### Sprint 1 (1-2주): 기반
- [ ] Next.js 프로젝트 초기화 + 랜딩 페이지
- [ ] Supabase 프로젝트 생성 + 스키마
- [ ] GitHub OAuth 로그인

### Sprint 2 (3-4주): 에이전트 코어
- [ ] FastAPI 서버 + 레포 연결 API
- [ ] 에이전트 코어 리팩토링 (단일 레포 분석 → PR 생성 파이프라인)
- [ ] Celery 워커 + 일간 스케줄러

### Sprint 3 (5-6주): 대시보드
- [ ] 대시보드 UI (실행 이력, PR 목록)
- [ ] 이메일 알림 (일간 리포트)
- [ ] 에러 핸들링 + 재시도 로직

### Sprint 4 (7-8주): 베타 런치
- [ ] 얼리 어답터 10명 온보딩
- [ ] 피드백 수집 + 버그 수정
- [ ] 랜딩 페이지 최종화 + waitlist

## 7. 핵심 리스크 및 대응

| 리스크 | 영향 | 대응 |
|--------|------|------|
| Claude API 비용 초과 | 수익성 악화 | 토큰 사용량 모니터링, 캐싱, 모델 선택 최적화 |
| PR 품질 불안정 | 사용자 이탈 | 자동 테스트 실행 후 PR 생성, 안전 체크리스트 |
| GitHub Rate Limit | 서비스 중단 | GitHub App으로 전환 (더 높은 rate limit) |
| 보안 (코드 접근) | 신뢰 문제 | 최소 권한 원칙, 감사 로그, 코드를 서버에 저장하지 않음 |

## 8. 결정 사항 요약

1. **프론트엔드**: Next.js 14 + Tailwind + shadcn/ui → Vercel 배포
2. **백엔드**: FastAPI (Python) → Railway 배포
3. **DB**: Supabase (PostgreSQL + Auth)
4. **에이전트**: Python + Claude API + Celery
5. **MVP 초기 비용**: ~$55-110/월 (10명 베타 기준)
6. **MVP 타임라인**: 8주 (4 스프린트)
7. **MVP 첫 목표**: 단일 레포, 일간 1 PR, 결과 대시보드
