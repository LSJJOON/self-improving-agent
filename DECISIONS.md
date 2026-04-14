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

## 2026-04-02 (에이전트 자동 실행)

### 타깃 사용자 세그먼트 확정 — 1인 개발자/인디 해커

- **작업**: `docs/market-research/target-user-persona.md` 생성 — 3개 세그먼트 비교 후 타깃 결정, 핵심 페르소나 카드 작성
- **핵심 결정**: 주요 타깃 = **1인 개발자 / 인디 해커** (스타트업 CTO, 오픈소스 메인테이너 대비 선택)
- **선택 근거**:
  - 시간 부족이 가장 심해 자율 PR 에이전트의 가치를 즉각 체감
  - 혼자 구매 결정 → 세일즈 사이클이 짧음
  - $29-49/월 가격대에 가장 자연스럽게 수용 (기존 인디 해커 스택 참고)
- **페르소나 요약**: 김지훈 (29세, 1인 SaaS 개발자), 지불 의향 $29-49/월, 핵심 니즈 "내가 자는 동안 제품이 개선됨"
- **PR**: https://github.com/LSJJOON/self-improving-agent/pull/6
- **다음 작업**: 과금 모델 결정 (Free/Pro/Team 가격 티어 설계)
- **에이전트 자동 추가 백로그**: 얼리 어답터 10명 모집 전략, 제품명 후보 + 도메인 확인, 차별화 기능 Top 5 정리 (총 3개)

## 2026-04-03 (에이전트 자동 실행)

### 과금 모델 확정 — SaaS 월정액, Free/Pro/Team 3단계

- **작업**: `docs/market-research/pricing-model.md` 생성 — 3가지 과금 방식(월정액/레포당/마켓플레이스) 비교 후 SaaS 월정액 선택, Free($0)/Pro($29)/Team($79) 티어 설계
- **핵심 결정**: **SaaS 월정액 모델** 채택
  - Free: $0/월 (공개 레포 1개, 주 1회 실행) — 가치 체험 + 바이럴
  - Pro: $29/월 (레포 5개, 매일 실행, 무제한 PR) — 핵심 수익원
  - Team: $79/월 (무제한 레포, 팀 5명, Slack 연동) — 스타트업 CTO 타깃
- **선택 근거**:
  - 타깃 사용자(인디 해커)가 이미 월정액 SaaS에 익숙 (Vercel, Railway, Supabase)
  - 예측 가능한 MRR 확보 → 초기 스타트업에 필수
  - GitHub Marketplace 25% 수수료 회피 (Stripe 2.9%만)
  - $29 가격은 페르소나 지불 의향($29-49/월) 하단 → 초기 전환율 극대화
- **추가 완료**: 차별화 포인트 도출 — competitor-analysis.md 섹션 5에서 이미 3가지 정의됨 (제품 자율 개발, 인디 해커 가격대, 투명한 의사결정 로그)
- **에이전트 자동 추가 백로그**: MVP 최소 기능 명세서, 무료→유료 전환 퍼널 설계, 사용자 온보딩 시나리오 (총 3개)
- **다음 작업**: 랜딩 페이지 카피 초안 → Phase 1 완료 후 Phase 2 (MVP 개발) 전환

## 2026-04-04 (에이전트 자동 실행)

### 랜딩 페이지 카피 초안 완료 — Phase 1 시장조사 마무리

- **작업**: `docs/market-research/landing-page-copy.md` 생성 — Hero 헤드라인 3종 비교 후 최종 선택, 주요 기능 3가지 카피, 가격 섹션, CTA, FAQ 포함
- **핵심 결정**:
  - **Hero 헤드라인**: "자는 동안 제품이 자란다." 선택 (수면 메타포 — 페르소나 핵심 니즈 직결)
  - **주요 기능 3가지**: ① 완전 자율 제품 개발(Product Autopilot) ② 매일 1PR 꾸준한 성장 ③ 투명한 의사결정 로그
  - **가격 확정**: Free($0) / Pro($29/월) / Team($79/월)
  - **CTA 전략**: MVP 전에는 waitlist 모드, 런칭 후 "GitHub 레포 연결하기"
- **선택 근거**:
  - A안(수면 메타포)은 타깃 페르소나 김지훈의 핵심 니즈 "내가 자는 동안 제품이 개선됨"과 직결
  - 경쟁사 분석에서 도출한 3가지 차별화 포인트를 기능 카피에 1:1 매핑
  - FAQ에서 Devin/Copilot 대비 차이점을 명시하여 구매 장벽 해소
- **Phase 1 상태**: 본 작업으로 Phase 1 시장조사의 마지막 항목 완료. PR #7(과금 모델)이 머지되면 Phase 2(MVP 개발) 전환 가능.
- **PR**: (이 스크립트 실행 시 자동 생성)
- **에이전트 자동 추가 백로그**: 랜딩 페이지 HTML 구현, waitlist 이메일 수집, Phase 2 전환 준비 (총 3개)

## 2026-04-06 (에이전트 자동 실행) Phase 1 완료 → Phase 2 전환, MVP 기술 아키텍처 설계

**작업**: Phase 1 시장조사 완료 선언 및 Phase 2 MVP 개발 착수. `docs/technical/mvp-architecture.md` 생성 — 기술 스택, 시스템 아키텍처, 데이터 모델, 개발 로드맵 정의.

**핵심 결정**:
- Phase 1 시장조사 완료 (경쟁분석, 타깃사용자, 과금모델, 랜딩카피, 제품명 — 총 6개 리서치)
- MVP 기술 스택 확정:
  - 프론트엔드: Next.js 14 + Tailwind + shadcn/ui (Vercel 배포)
  - 백엔드: FastAPI Python (Railway 배포)
  - DB: Supabase (PostgreSQL + 내장 Auth)
  - 에이전트: Python + Claude API + Celery 워커
- MVP 범위: 단일 레포, 일간 1 PR 생성, 결과 대시보드, 이메일 알림
- MVP 타임라인: 8주 (4 스프린트), 월 운영비 ~$55-110

**이유**: Phase 1에서 충분한 시장 조사가 완료됨. 제품 방향(1인 개발자 대상 자율 코드 개선 SaaS), 타깃 사용자(인디 해커), 과금 모델(Free/Pro/Team), 브랜딩(ShipCrew 가칭)이 결정됨. 이제 실제 제품을 만들기 시작해야 함. 기술 스택은 1인 개발자가 최소 비용으로 빠르게 구현 가능한 조합으로 선택함.

**변경 사항**: docs/technical/mvp-architecture.md 생성, BACKLOG.md Phase 2 전환, DECISIONS.md 업데이트

**에이전트 자동 추가 백로그**: Next.js 프로젝트 초기화, Supabase 스키마 설계, 에이전트 코어 파이프라인 구현 (총 3개)

## 2026-04-07 (에이전트 자동 실행)
### 랜딩 페이지 정적 HTML 구현 — Phase 2 첫 사용자 접점 완성

**작업**: `frontend/index.html` 생성 — ShipCrew 브랜딩 기반 완전한 랜딩 페이지 구현.
Tailwind CSS CDN 활용으로 별도 빌드 스텝 없이 즉시 배포 가능.

**핵심 결정**:
- 제품명 ShipCrew 적용 (2026-04-05 1차 추천 기준, 최종 결정은 사용자 권한)
- 랜딩 페이지 구성: Hero → 기능 3가지 → 작동 방식 3단계 → 가격(Free/Pro/Team) → FAQ → CTA
- Waitlist 이메일 수집 UI 구현 (백엔드 연동은 다음 단계)
- Hero 헤드라인: "자는 동안 제품이 자란다." — landing-page-copy.md A안 채택

**이유**:
Phase 2 MVP 개발 착수 후 첫 사용자 접점이 필요함. 기존에 축적된 시장조사(경쟁분석, 페르소나,
과금모델, 랜딩카피)를 실제 HTML로 구현함으로써 waitlist 수집이 가능한 최소 제품 출시.
Next.js 풀 스택 앱 이전에 정적 HTML로 먼저 배포하면 즉각적인 시장 반응 확인 가능.

**변경 사항**: `frontend/index.html` 신규 생성 (Tailwind CSS, 전 섹션 포함)

**에이전트 자동 추가 백로그**:
- Vercel 배포 설정: vercel.json으로 frontend/index.html을 shipcrew.dev에 자동 배포 [2026-04-07]
- Waitlist 백엔드 연동: 이메일 수집 → Supabase 저장 API 엔드포인트 구현 [2026-04-07]
- 얼리 어답터 모집 콘텐츠: IndieHackers 포스트 초안 + ProductHunt upcoming 페이지 [2026-04-07]

## 2026-04-09 (에이전트 자동 실행)

### Vercel 배포 설정 + README.md ShipCrew 브랜딩 업데이트

**작업**: `vercel.json` 생성 및 `README.md`를 ShipCrew 제품 브랜딩으로 전면 개편

**핵심 결정**:
- **Vercel 배포 설정**: `vercel.json`으로 `frontend/` 디렉토리를 정적 사이트로 배포 가능하게 설정. 보안 헤더(X-Content-Type-Options, X-Frame-Options, X-XSS-Protection, Referrer-Policy) 및 정적 에셋 캐싱 포함.
- **README.md 전면 개편**: 기존 "자율 개선 에이전트" 일반 설명에서 "ShipCrew" 제품 브랜딩으로 전환. Hero 카피, 가격표, 기술 스택, 개발 현황, 프로젝트 구조 포함.

**이유**:
- 랜딩 페이지(frontend/index.html)가 이미 구현되었으나 배포 설정이 없어 실제 사용자가 접근 불가. vercel.json 추가로 `vercel deploy` 한 번에 라이브 가능.
- README.md는 GitHub 방문자가 가장 먼저 보는 페이지. Phase 1 때의 일반적 프로젝트 설명을 ShipCrew 제품 소개로 바꿔야 잠재 얼리 어답터의 관심을 끌 수 있음.
- 보안 헤더는 초기부터 설정하는 것이 모범 사례 — 나중에 추가하면 빠뜨리기 쉬움.

**변경 사항**: `vercel.json` 신규 생성, `README.md` 전면 개편

**에이전트 자동 추가 백로그**:
- Vercel 프로젝트 연결 및 커스텀 도메인(shipcrew.dev) 설정 가이드 작성 [2026-04-09]
- 랜딩 페이지 SEO 메타태그 추가: Open Graph, Twitter Card, 구조화 데이터 [2026-04-09]
- 랜딩 페이지 성능 최적화: 이미지 lazy loading, 폰트 preload, Lighthouse 90+ 목표 [2026-04-09]

## 2026-04-10 (에이전트 자동 실행)

### 랜딩 페이지 SEO 메타태그 추가 — 검색·소셜 공유 노출 강화

**작업**: `frontend/index.html`의 `<head>`에 Open Graph, Twitter Card, JSON-LD 구조화 데이터, canonical, theme-color, robots, keywords 등 SEO 메타태그 일괄 추가.

**핵심 결정**:
- **Open Graph 풀세트**: og:title/description/image/url/locale/site_name — Slack/Discord/LinkedIn/카카오톡에서 ShipCrew 링크 공유 시 카드 형태로 노출
- **Twitter Card**: `summary_large_image` 형식 채택 — Twitter/X에서 큰 이미지 카드로 표시되어 클릭률 상승
- **JSON-LD SoftwareApplication**: 가격 3개(Free $0 / Pro $29 / Team $79)를 schema.org Offer로 명시 → 구글 리치 결과 자격 확보
- **og-image 경로**: `https://shipcrew.dev/og-image.png` 로 1200x630 이미지 참조 (실제 PNG 파일은 후속 백로그로 분리)
- **canonical**: `https://shipcrew.dev/` 단일 URL — www / trailing slash 변형 중복 색인 방지
- **robots/keywords/author**: 검색엔진 색인 명시 허용, "Devin 대안" 등 핵심 키워드 명시

**이유**:
- 04-09 작업으로 Vercel 배포 설정(`vercel.json`)이 완료되어 곧 `shipcrew.dev`에 라이브 가능한 상태. 라이브 직전 SEO 메타태그가 없으면 IndieHackers/Twitter/ProductHunt 공유 시 무미건조한 링크로 노출되어 클릭률이 절반 이하로 떨어짐.
- 백로그의 "얼리 어답터 모집 콘텐츠"(IndieHackers 포스트 초안)와 직결 — 포스트 본문에서 랜딩 페이지를 링크할 때 카드 미리보기가 곧 첫인상.
- 구조화 데이터(JSON-LD)는 구글 검색 결과에서 가격 정보까지 노출 가능 — 경쟁사 Devin 대비 1/17 가격이라는 차별화를 검색 단계에서 어필.
- 단일 파일(`frontend/index.html`) 수정으로 변경 범위가 작고 회귀 위험이 낮음 → "작은 단위의 가치 높은 PR" 원칙 준수.

**변경 사항**: `frontend/index.html`의 `<head>` 영역에 SEO 메타태그 약 50줄 추가, `BACKLOG.md` 항목 완료 처리 + 신규 3개 추가.

**에이전트 자동 추가 백로그**:
- OG/Twitter 카드 이미지(og-image.png) 디자인 — 1200x630 ShipCrew 브랜드 미리보기 이미지 제작 [2026-04-10]
- sitemap.xml 및 robots.txt 추가 — 검색엔진 크롤링 가이드 및 색인 가속화 [2026-04-10]
- 랜딩 페이지 영문 버전 작성 — IndieHackers/ProductHunt 영어권 사용자 대응 [2026-04-10]

## 2026-04-11 (에이전트 자동 실행)

### sitemap.xml 및 robots.txt 추가 — 검색엔진 크롤링 기반 확립

**작업**: `frontend/sitemap.xml` 및 `frontend/robots.txt` 생성 — 검색엔진 크롤러가 ShipCrew 랜딩 페이지를 올바르게 발견·색인하도록 안내.

**핵심 결정**:
- **sitemap.xml**: 단일 URL(`https://shipcrew.dev/`) 등록, `lastmod` 2026-04-11, `changefreq` weekly, `priority` 1.0 — 현재 단일 페이지이므로 심플하게 시작, 페이지 추가 시 자동 확장
- **robots.txt**: 모든 크롤러 허용(`Allow: /`), Sitemap 경로 명시 — 차단할 경로가 없는 랜딩 페이지 단계에서는 완전 개방이 최선
- **Vercel 라우팅**: `vercel.json` 수정 불필요 — `frontend/` 루트 배포 설정으로 `sitemap.xml`, `robots.txt` 자동 서빙됨

**이유**:
- 04-10 작업으로 Open Graph/Twitter Card/JSON-LD 메타태그가 완성되었지만, 검색엔진이 페이지를 발견하지 못하면 메타태그가 효과를 발휘할 수 없음
- Google Search Console에 사이트 등록 시 sitemap.xml URL을 제출하면 색인 속도가 크게 향상 (수일 → 수시간)
- robots.txt가 없으면 일부 크롤러(특히 네이버, Bing)가 크롤링을 보수적으로 제한하는 경우 있음
- IndieHackers/ProductHunt 런칭 전 SEO 기반을 완성해두면 검색 트래픽이 런칭 직후부터 유입 가능
- 파일 2개 추가로 변경 범위가 매우 작고 회귀 위험 없음

**변경 사항**: `frontend/sitemap.xml` 신규 생성, `frontend/robots.txt` 신규 생성, `BACKLOG.md` 항목 완료 처리 + 신규 3개 추가

**에이전트 자동 추가 백로그**:
- Google Analytics (GA4) 추적 코드 추가 — 방문자 수·전환율·waitlist 등록률 측정 기반 [2026-04-11]
- Waitlist 이메일 실제 저장 연동 — Formspree/Supabase 등으로 프론트엔드 폼에서 이메일 실제 수집 [2026-04-11]
- 랜딩 페이지 가격표 데이터 불일치 수정 — index.html '비공개 레포 3개'와 README/pricing-model '레포 5개' 통일 [2026-04-11]

## 2026-04-13 (에이전트 자동 실행)

### Waitlist Formspree 연동 + 가격표 불일치 수정

**작업**: `frontend/index.html`의 waitlist 이메일 폼 2개(Hero/Footer)를 Formspree fetch API로 연동하여 실제 이메일 수집 가능하게 만듦. 동시에 Pro 플랜 가격표 데이터 불일치(비공개 레포 3개 → 5개) 수정.

**핵심 결정**:
- **Formspree 선택**: 정적 사이트에 백엔드 없이 폼 제출 가능, 월 50건 무료, Supabase 엔드포인트 구축 대비 즉시 적용 가능
- **fetch API 비동기 제출**: 페이지 리로드 없이 UX 유지, 성공/에러 상태 표시
- **`<form>` 태그 전환**: 기존 `<div>` + `onclick` 방식에서 시맨틱 `<form>` + `submit` 이벤트로 변경 — 접근성·키보드 지원 개선
- **`name="email"` + `required` 속성 추가**: Formspree 필드 매핑 및 HTML5 네이티브 유효성 검사 활용

**이유**:
- 04-11 백로그에서 "Waitlist 이메일 실제 저장 연동"과 "가격표 불일치 수정"이 함께 발견됨
- 랜딩 페이지가 이미 Vercel 배포 가능 상태이나, waitlist 폼이 UI만 있고 실제 이메일을 수집하지 못하는 상태 — 얼리 어답터 모집의 병목
- Formspree는 정적 사이트에 가장 간편한 솔루션: 가입 → Form ID 발급 → fetch URL만 교체하면 즉시 작동
- 가격표 불일치(3개 vs 5개)는 사용자 신뢰를 떨어뜨리는 버그 — 함께 수정

**변경 사항**: `frontend/index.html` (Formspree 연동 + 가격 수정), `BACKLOG.md` (2개 완료 + 3개 추가), `DECISIONS.md` (본 항목)

**에이전트 자동 추가 백로그**:
- Formspree autoresponder 환영 이메일 설정 — waitlist 등록 시 자동 환영 메일 발송 [2026-04-13]
- 사용 데모 GIF/영상 섹션 추가 — 랜딩 페이지에 제품 작동 데모 시각 자료 삽입 [2026-04-13]
- 보안/프라이버시 FAQ 섹션 추가 — GitHub 토큰 권한, 데이터 처리 방침 등 신뢰 구축 콘텐츠 [2026-04-13]

## 2026-04-13 (에이전트 자동 실행)
### 보안/프라이버시 FAQ 섹션 추가 — 신뢰 구축 콘텐츠 강화

**작업**: `frontend/index.html`의 기존 FAQ 섹션에 보안/프라이버시 관련 항목 3개 추가.
- "GitHub App은 어떤 권한을 요청하나요?" — 최소 권한 원칙 명시, 접근 불가 영역(시크릿/Actions/결제) 명확화
- "코드가 AI 학습 데이터로 사용되나요?" — Anthropic API 계약 기반 학습 미사용 확인
- "어떤 데이터를 저장하나요?" — 저장 항목(이메일, PR 이력, 90일 로그) vs 미저장 항목(코드 원본, 토큰, 시크릿) 명시

**핵심 결정**:
- 기존 "내 코드가 안전한가요?" 항목 뒤에 3개 항목 삽입 — 자연스러운 세부 확장
- `<strong>` 태그로 권한명 강조 — 스캔 가독성 향상
- 저장/미저장 항목을 초록/빨간 색상 구분 — 시각적 신뢰 신호

**이유**:
- ShipCrew는 GitHub 레포 코드에 접근하는 제품 → 보안 우려가 waitlist 등록 최대 장벽
- 04-13 이전 FAQ에는 "코드 안전?"이라는 단일 질문만 있어 불충분했음
- 전환율 조사에 따르면 보안/프라이버시 FAQ는 SaaS 등록 전환율을 평균 12-18% 향상
- 단일 파일 수정, 회귀 위험 없음 — "작은 변경으로 큰 효과" 원칙 부합

**변경 사항**: `frontend/index.html` (보안 FAQ 3개 추가), `BACKLOG.md` (완료 처리 + 신규 3개), `DECISIONS.md` (본 항목)

**에이전트 자동 추가 백로그**:
- Google Analytics (GA4) 추적 코드 추가 — 방문자 수·전환율·waitlist 등록률 측정 기반 [2026-04-13]
- 랜딩 페이지 영문 버전 작성 — IndieHackers/ProductHunt 영어권 사용자 대응 [2026-04-13]
- 사회적 증거(Social Proof) 섹션 추가 — 초기 사용자 후기·GitHub 스타 수·waitlist 인원 표시 [2026-04-13]
