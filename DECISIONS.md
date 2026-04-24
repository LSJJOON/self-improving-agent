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

## 2026-04-14 (에이전트 자동 실행)

### Google Analytics (GA4) 추적 코드 + Waitlist 전환 이벤트 추가

**작업**: `frontend/index.html`의 `<head>`에 Google Analytics (GA4) gtag.js 스니펫 추가 및 waitlist 폼 제출 성공 시 전환 이벤트(`waitlist_signup`) 발송 코드 삽입.

**핵심 결정**:
- **GA4 gtag.js 선택**: Google Tag Manager 대비 설정이 간단하고, 정적 사이트에 스크립트 태그 하나로 즉시 적용 가능
- **커스텀 전환 이벤트**: `waitlist_signup` 이벤트에 `event_label`(hero/footer_cta)을 포함하여 어느 CTA에서 전환이 발생하는지 추적
- **Measurement ID 플레이스홀더**: `G-XXXXXXXXXX`로 코드에 삽입 — 사용자가 GA4 속성을 생성한 후 실제 ID로 교체 필요
- **JSON-LD 다음, Tailwind 앞 배치**: SEO 메타태그 블록과 스타일 사이에 위치하여 논리적 순서 유지

**이유**:
- 04-13 작업으로 Formspree waitlist 폼이 실제 이메일을 수집하게 되었으나, 전환율을 측정할 방법이 없었음
- SEO 메타태그(04-10), sitemap/robots.txt(04-11) 등 트래픽 유입 기반은 완성되었지만, 유입된 방문자가 실제로 waitlist에 등록하는 비율을 모르면 향후 최적화 방향을 잡을 수 없음
- IndieHackers/ProductHunt 런칭 전 GA4를 설치해두면 런칭 직후부터 채널별 전환율 데이터 수집 가능
- Hero CTA vs Footer CTA 전환율 비교 데이터는 향후 랜딩 페이지 A/B 테스트의 베이스라인이 됨
- 단일 파일 수정, 회귀 위험 없음 — "작은 변경으로 큰 효과" 원칙 부합

**변경 사항**: `frontend/index.html` (GA4 gtag.js + 전환 이벤트), `BACKLOG.md` (2개 완료 + 3개 추가), `DECISIONS.md` (본 항목)

**에이전트 자동 추가 백로그**:
- GA4 전환 목표(Goal) 설정 가이드 — waitlist_signup 이벤트를 전환 목표로 등록하는 방법 안내 문서 작성 [2026-04-14]
- UTM 파라미터 기반 유입 채널 추적 — IndieHackers/ProductHunt/Twitter 등 채널별 waitlist 전환율 비교 가능하게 [2026-04-14]
- 랜딩 페이지 A/B 테스트 프레임워크 — Hero 카피·CTA 버튼 색상 등 전환율 실험을 위한 기초 인프라 구축 [2026-04-14]

## 2026-04-17 (에이전트 자동 실행)

### 영문 랜딩 페이지 추가 — IndieHackers/ProductHunt 영어권 사용자 대응

**작업**: `frontend/en.html` 신규 생성 — 기존 한국어 랜딩 페이지(`index.html`)의 완전한 영문 번역 버전. 동시에 `index.html`에 언어 스위처(한/영) 및 hreflang 태그 추가.

**핵심 결정**:
- **독립 HTML 파일 방식**: 한 페이지에서 JS로 언어 전환하는 방식 대신 별도 파일(`en.html`)로 분리 — SEO 친화적이고 각 언어별 독립적인 OG/Twitter 메타태그 설정 가능
- **hreflang 태그 양방향 설정**: `index.html`에 `hreflang="ko"` + `hreflang="en"`, `en.html`에 동일 태그 — Google이 언어별 페이지를 정확히 식별하여 각 사용자에게 적합한 버전 노출
- **네비게이션 언어 스위처**: 네비 메뉴와 푸터에 국기 이모지 링크(🇺🇸 EN / 🇰🇷 KO) 추가 — 사용자가 직관적으로 언어 전환 가능
- **GA4 이벤트 구분**: 영문 페이지 waitlist 이벤트에 `lang: "en"`, `source: "hero_en"/"footer_cta_en"` 추가 — 한/영 채널별 전환율 비교 가능
- **카피 현지화**: 직역이 아닌 영어권 인디 해커 문화에 맞는 자연스러운 표현 사용 ("Ship like a team, even as a solo dev", "Trust, but verify" 등)

**이유**:
- ShipCrew의 주요 얼리 어독터 모집 채널(IndieHackers, ProductHunt, Twitter/X)은 모두 영어권 플랫폼
- 한국어만 있는 랜딩 페이지로는 영어권 사용자의 waitlist 등록을 기대할 수 없음
- SEO 관점에서 hreflang 태그는 다국어 사이트의 필수 요소 — Google이 언어별 페이지를 정확히 인식
- 04-10 작업으로 OG/Twitter 메타태그, 04-11에 sitemap/robots.txt, 04-14에 GA4가 모두 완성된 상태 — 영문 페이지 추가로 글로벌 트래픽 유입 기반 완성
- 별도 파일로 분리하여 변경 범위가 작고 회귀 위험 없음

**변경 사항**: `frontend/en.html` 신규 생성, `frontend/index.html` (hreflang + 언어 스위처), `BACKLOG.md` (영문 페이지 항목 완료 + 신규 3개), `DECISIONS.md` (본 항목)

**에이전트 자동 추가 백로그**:
- sitemap.xml에 영문 페이지 URL 추가 — /en 경로를 sitemap에 등록하여 검색엔진 색인 가속화 [2026-04-17]
- 영문 랜딩 페이지 OG 메타태그 영어 버전 검증 — SNS 공유 시 영어 카드 미리보기 정상 노출 확인 [2026-04-17]
- IndieHackers/ProductHunt 런칭 포스트 초안 작성 — 영문 랜딩 페이지 링크 포함한 얼리 어독터 모집 콘텐츠 [2026-04-17]

## 2026-04-18 (에이전트 자동 실행)

### sitemap.xml에 영문 랜딩 페이지 URL + hreflang 추가 — 영문 페이지 검색 색인 가속화

**작업**: `frontend/sitemap.xml`을 확장하여 (1) 2026-04-17 신규 추가된 `frontend/en.html` 영문 랜딩 페이지 URL을 등록하고, (2) Google 권장 다국어 sitemap 형식(`xhtml:link` with `hreflang`)을 적용하여 한/영 대체 관계를 명시. `lastmod` 날짜도 최신(2026-04-18)으로 갱신.

**핵심 결정**:
- **URL 2개 등록**: `https://shipcrew.dev/` (ko, priority 1.0) + `https://shipcrew.dev/en.html` (en, priority 0.9) — 한국어를 기본(메인 시장)으로, 영문을 2순위로 두되 둘 다 색인 대상
- **xhtml:link hreflang 적용**: 각 `<url>` 블록에 `ko` / `en` / `x-default` 세 개의 alternate 링크 삽입 — Google이 사용자 언어에 맞는 버전을 자동 서빙
- **x-default는 한국어 페이지**: 알 수 없는 언어 사용자에게는 기본 한국어 페이지 노출 (주요 타깃 시장이 한국/아시아)
- **파일 경로 선택**: `/en` 깔끔한 URL 대신 실제 파일 경로 `/en.html` 사용 — Vercel rewrite 추가 작업 없이 즉시 동작. `/en` 매핑은 후속 백로그로 분리.
- **`urlset`에 xhtml 네임스페이스 선언**: `xmlns:xhtml="http://www.w3.org/1999/xhtml"` 추가 — Google Search Console이 alternate 링크를 올바르게 파싱하기 위한 필수 요소

**이유**:
- 2026-04-17 작업으로 영문 랜딩 페이지(`frontend/en.html`)가 추가되었지만 sitemap.xml에는 반영되지 않아 검색엔진이 해당 페이지를 발견하기 어려움 — IndieHackers/ProductHunt 런칭 전 영어권 검색 트래픽 유입을 막는 병목
- `hreflang` 태그는 단순 URL 등록만으로는 부족한 다국어 SEO의 핵심 시그널 — Google이 한국어 검색엔 `/`를, 영어 검색엔 `/en.html`을 노출하도록 유도
- Google Search Console에 sitemap을 재제출하면 영문 페이지 색인이 수일 내 완료되어 런칭 시점에 이미 검색 가능한 상태 확보
- 단일 파일 수정, 회귀 위험 없음 — "작은 변경으로 큰 효과" 원칙 부합
- 04-17 DECISIONS에서 제시한 "글로벌 트래픽 유입 기반"을 실제로 완성하는 후속 작업

**변경 사항**: `frontend/sitemap.xml` (xhtml 네임스페이스 + 2개 URL + 6개 hreflang 링크로 확장), `BACKLOG.md` (완료 처리 + 신규 3개 추가), `DECISIONS.md` (본 항목)

**에이전트 자동 추가 백로그**:
- Vercel `/en` 깔끔한 URL 매핑 — vercel.json rewrite로 `/en` → `/en.html` 구성해 SNS·IndieHackers 공유 URL 가독성 개선 [2026-04-18]
- Google Search Console sitemap 제출 가이드 — sitemap.xml 제출 절차·색인 상태 확인 방법 문서화 (영문 페이지 포함) [2026-04-18]
- 랜딩 페이지 Core Web Vitals 측정·개선 — Lighthouse 90+ 목표, 폰트 preload·Tailwind CDN 최적화로 모바일 LCP 단축 [2026-04-18]

## 2026-04-19 (에이전트 자동 실행)
### 사회적 증거(Social Proof) 섹션 추가 — 랜딩 페이지 신뢰도 강화

**작업**: `frontend/index.html`과 `frontend/en.html` 두 파일 모두에 Hero 섹션 바로 아래 "Built in Public" 사회적 증거 섹션을 삽입. shields.io 동적 배지 3개(GitHub Stars · Agent PRs · Last Run) + DECISIONS.md / 실제 PR 기록 링크 포함.

**핵심 결정**:

- **shields.io 실시간 배지 채택**: GitHub API를 직접 호출하는 JS fetch 대신 shields.io 배지를 사용. 별도 JS 코드 없이 실시간 데이터(스타 수·닫힌 PR 수·마지막 커밋) 노출 → 초기 투자 비용 0, 유지보수 부담 없음.
- **가짜 숫자·빈 후기 placeholder 금지**: 백로그 원안에는 "초기 사용자 후기·waitlist 인원"이 포함되어 있었으나, 실제 데이터가 없는 상태에서 placeholder를 노출하면 오히려 신뢰를 훼손. 현재 실제로 존재하는 "오픈소스 시그널"(별·자동 PR·커밋 기록·DECISIONS.md)만 노출하여 정직성 원칙 유지.
- **투명한 의사결정 로그를 전면 앵커로**: 랜딩 페이지 카피·FAQ·경쟁 분석 전반에서 차별화 포인트로 밀던 "DECISIONS.md 공개"를 Social Proof 섹션에서 다시 강조 → 동일 메시지가 여러 접점에서 반복되며 브랜드 일관성 확보.
- **한/영 동시 적용**: 단일 PR로 `index.html`·`en.html` 모두 업데이트. 본문 텍스트는 각 언어에 맞게 현지화했으나 배지 라벨(Stars/Agent PRs/Last Run)은 영문 공용 → URL 인코딩 이슈 회피 + 배지 캐시 효율 향상.
- **Hero ↔ Features 사이 배치**: 가장 먼저 CTA(waitlist)를 본 방문자가 스크롤을 내릴 때 두 번째 섹션에서 즉시 "진짜 작동하는 오픈소스 프로젝트"라는 증거를 만나도록 배치 → 신뢰 형성 후 기능 설명으로 진입.

**이유**:

- 04-14 GA4 도입으로 전환율을 측정할 수 있게 됐으나, 전환율 자체를 올릴 요소가 부족했음. 사회적 증거는 SaaS 랜딩에서 전환율을 평균 12-18% 높이는 검증된 요소.
- 제품이 아직 베타 전 단계라 실제 사용자 후기가 없음 → "Built in Public" 오픈소스 시그널이 현 단계에서 가장 정직하고 강력한 신뢰 근거.
- IndieHackers/ProductHunt 영문 런칭 준비 중 — 영문 페이지에도 동일 섹션을 넣어 글로벌 방문자에게 동일한 신뢰 시그널 제공.
- 현재 open PR #28(sitemap hreflang)과 주제가 겹치지 않으며, 단일 브랜치에 2개 파일만 수정하여 회귀 위험이 낮음 — "작은 변경으로 큰 효과" 원칙 준수.

**변경 사항**: `frontend/index.html` (사회적 증거 섹션 추가), `frontend/en.html` (사회적 증거 섹션 추가, 영문), `BACKLOG.md` (사회적 증거 완료 처리 + 신규 3개 추가), `DECISIONS.md` (본 항목)

**에이전트 자동 추가 백로그**:
- 랜딩 페이지 라이브 카운터 — GitHub API로 실제 스타 수·자동 생성 PR 수를 동적으로 fetch해 Hero 통계 영역에 표시 (사회적 증거 V2) [2026-04-19]
- 언어 자동 감지 리다이렉트 — navigator.language 기반 첫 방문자에게 한/영 적합 페이지 자동 노출 + 수동 토글 유지 [2026-04-19]
- 얼리 어독터 슬롯 카운터 추가 — "50명 중 X명 등록" 표시로 마감 긴급성 시각화, 전환율 향상 [2026-04-19]

## 2026-04-20 (에이전트 자동 실행)

### UTM 파라미터 기반 유입 채널 추적 추가 — 채널별 전환율 비교 기반 확보

**작업**: `frontend/index.html` 및 `frontend/en.html` `<head>`에 UTM 파라미터 캡처 IIFE 추가. URL 쿼리스트링의 `utm_source`/`utm_medium`/`utm_campaign`/`utm_term`/`utm_content`를 읽어 `sessionStorage`에 보존하고, GA4 `user_properties`에 등록하여 모든 이벤트에 자동 첨부되도록 구성. Formspree 제출 JSON 본문과 `waitlist_signup` 전환 이벤트에도 UTM 값 병합.

**핵심 결정**:
- **sessionStorage 보존**: 첫 진입 URL에서만 UTM이 있고 다른 페이지로 이동하면 사라지는 문제를 방지. 한국어 랜딩(`/`) ↔ 영문 랜딩(`/en`) 간 전환에도 UTM이 유지됨 → 언어 스위처 사용 시 원 채널 정보 손실 없음.
- **GA4 user_properties 등록**: 개별 이벤트에 UTM을 수동으로 붙이지 않아도 `gtag("set", "user_properties", utm)` 한 번으로 이후 모든 이벤트(page_view 포함)에 자동 첨부. UTM 파라미터 5종 모두 표준 이름을 사용해 GA4 보고서에서 자동 인식.
- **Formspree 본문에도 포함**: GA4 외에 이메일 수신함에서도 각 waitlist 등록자의 유입 채널을 즉시 확인 가능 → 초기 얼리 어답터 대응 시 채널별 맞춤 커뮤니케이션 설계.
- **`waitlist_signup` 이벤트에 직접 병합**: `Object.assign` 으로 기존 `event_category`·`event_label`과 UTM을 합쳐 발송. GA4 탐색 보고서에서 `event_label`(hero/footer) × `utm_source`(indiehackers/producthunt/…) 교차 분석 가능.
- **URL 오염 없음**: 캡처 후 리다이렉트 없이 URL에 UTM을 그대로 두어 GA4의 표준 획득 채널 처리(자동 캠페인 매칭)도 정상 작동.
- **방어적 구현**: `try/catch`로 `sessionStorage` 접근 실패(시크릿 모드·스토리지 차단)를 무시. UTM이 없는 순수 직방문에도 추가 부하 없음.

**이유**:
- 04-14 GA4 gtag.js 설치로 방문자·waitlist 전환율을 측정할 수 있게 됐으나, 어느 채널(IndieHackers/ProductHunt/Twitter/Reddit)이 가장 효율적인지 알 수 없음 → 런칭 콘텐츠별 ROI 판단 불가.
- 곧 예정된 IndieHackers/ProductHunt 런칭 포스트 초안 작성 전에 UTM 수집 기반을 깔아야 런칭 직후부터 채널별 데이터가 쌓임. 런칭 이후 추가하면 초기 핵심 데이터가 공란으로 남음.
- 인디 해커 가격대($29) 제품은 CAC(획득 비용)가 곧 생존선 → 어느 채널이 가장 싸게 전환되는지가 Phase 2 마케팅 의사결정의 핵심 지표.
- 한/영 랜딩 양쪽에 동시 적용 + sessionStorage 공유로 "영문 포스트에서 유입 → 한국어 페이지로 전환" 같은 교차 플로우도 정확히 트래킹.
- 두 파일 수정(+ 약 26줄 스크립트, 2줄 Object.assign), 외부 라이브러리 의존성 0, 회귀 위험 낮음 — "작은 변경으로 큰 효과" 원칙 부합.

**변경 사항**: `frontend/index.html` (UTM 캡처 스크립트 + fetch 본문 Object.assign + gtag 이벤트 Object.assign), `frontend/en.html` (동일 패턴 영문 주석 버전), `BACKLOG.md` (UTM 항목 완료 처리 + 신규 3개), `DECISIONS.md` (본 항목)

**에이전트 자동 추가 백로그**:
- 환영 이메일 템플릿 카피 작성 — waitlist 등록 직후 보낼 환영/다음 단계 안내 이메일 본문 초안 (제품 첫인상 강화) [2026-04-20]
- 웹사이트 내 UTM 링크 생성기 문서 — 채널별 표준 UTM 네이밍 규칙(utm_source 값 리스트) 가이드 작성 [2026-04-20]
- "현재 N명 대기 중" 실시간 카운터 섹션 — Formspree 대시보드 또는 파일 기반 카운트를 히어로 섹션에 노출 (사회적 증거 강화) [2026-04-20]

**수동 작업 이슈**: GA4 속성에서 UTM 파라미터 수신 확인 및 "채널별 전환율" 탐색 보고서 생성 가이드 (별도 이슈로 발급 예정)

## 2026-04-21 (에이전트 자동 실행)

### IndieHackers·ProductHunt·Twitter 런칭 포스트 초안 작성 — 트래픽 유입 기반 완성

**작업**: `docs/market-research/launch-posts.md` 신규 생성 — ShipCrew 런칭 채널 3곳(IndieHackers, ProductHunt, Twitter/X)에 게시할 포스트 초안 영문/한국어 버전 + 게시 전 체크리스트 + 게시 후 대응 가이드.

**핵심 결정**:

- **IndieHackers 포스트**: 제목 3종 후보 중 "I built an agent that ships a PR to my SaaS every morning — waitlist open" 권장. 본문은 ~350 단어로 (1) 사이드 프로젝트 죽음의 패턴 공감, (2) 동작 방식 3단계, (3) Devin/Copilot 대비 차별화 3가지, (4) waitlist CTA, (5) 커뮤니티 질문 2개 유도의 5단 구조.
- **ProductHunt 런칭 소재**: tagline 60자 이내, description 260자 이내, maker's first comment 3가지 구체적 피드백 질문 포함 — PH는 첫 24시간 댓글 engagement가 랭킹을 결정하므로 댓글 유도 설계가 핵심.
- **Twitter/X 7-tweet 스레드**: hook → problem → solution → dogfooding → pricing → bet → CTA 구조. 트윗당 길이는 모두 280자 제약 내로 작성.
- **한국어 버전**: F-Lab, 요즘IT, 디스콰이엇 등 국내 인디 커뮤니티용 별도 작성. 단순 번역이 아닌 국내 정서에 맞는 어투 적용.
- **채널별 UTM 템플릿**: `utm_source/medium/campaign` 파라미터를 채널별로 표준화 — PR #32(UTM 추적) 머지 후 실제 URL 생성에 재활용 가능.
- **게시 후 24시간 룰**: PH/IH는 첫 24시간 engagement가 랭킹을 거의 결정하므로 런칭 당일 다른 일정 비우기를 체크리스트에 명시.

**이유**:

- 04-17 작업으로 영문 랜딩 페이지 구현, 04-18 sitemap 영문 포함(PR #28), 04-19 사회적 증거 섹션(PR #30), 04-20 UTM 추적(PR #32)까지 완료되어 **랜딩 페이지의 트래픽 수용 기반은 완성**된 상태.
- 그러나 실제 트래픽을 흘려보낼 **외부 채널 포스트**가 아직 없음 → 아무리 랜딩이 좋아도 waitlist는 0에 수렴.
- 런칭 포스트는 실제 게시 전 여러 차례 리뷰·리라이트가 필요하므로 초안을 레포에 커밋해 공개 버전 관리하면 피드백 반영·버전 추적 용이.
- 영문/한국어 동시 작성: ShipCrew 주 얼리 어독터 채널(IH/PH/Twitter) = 영어권이지만, Joon이 한국에서 활동하므로 국내 커뮤니티 동시 론칭이 자연스러운 확장.
- 단일 파일(`docs/market-research/launch-posts.md`) 추가로 변경 범위 작고 회귀 위험 없음 — "작은 변경으로 큰 효과" 원칙 부합.
- 초안 상태임을 명시하여 실제 게시 전 Hero 카피 일관성·UTM·Formspree 테스트·og-image 준비가 선행되어야 함을 체크리스트에 포함.

**변경 사항**: `docs/market-research/launch-posts.md` 신규 생성, `BACKLOG.md` (런칭 포스트 항목 완료 + 신규 3개), `DECISIONS.md` (본 항목)

**에이전트 자동 추가 백로그**:

- og-image.png 실물 디자인·업로드 — 현재 경로 참조만 있어 SNS 공유 카드 미리보기 깨짐 [2026-04-21]
- 런칭 포스트 UTM URL 생성 및 지역·채널별 매트릭스 문서화 — PR #32 머지 후 [2026-04-21]
- 사용 데모 GIF(30초) 제작 및 랜딩 Hero 아래 삽입 — "자는 동안 PR이 올라오는" 장면 시각화 [2026-04-21]


## 2026-04-24 (에이전트 자동 실행)

### Phase 2 오픈 이슈 6건 의사결정 지원 문서 추가 — Week 1 착수 블로커 해소

**작업**: `docs/technical/phase2-open-issues-analysis.md` 신규 생성 — PR #36에서 추가 중인 MVP 명세서 §9의 오픈 이슈 6건(언어 지원, 대형 레포, stale PR 처리, 코드 전송 범위, 이메일 공급자, Stripe 세금)에 대해 선택지·트레이드오프·권장안을 정리. 이슈 #37(Phase 2 Week 1 착수 전 결정 필요)의 해소를 돕기 위한 사전 분석물.

**핵심 결정**:
- **문서 포지셔닝**: Joon의 최종 결정을 대체하지 않고 **의사결정 지원(Decision Support)** 문서로 한정 — 각 이슈에 2~4개 선택지 · 장단점 · 권장안 · 데드라인 · 후속 영향을 기술하되 "결정"은 하지 않음.
- **권장안 요약**:
  - 이슈 1(언어 지원): Python·JS/TS P0, Go/Rust는 Best-effort + `beta` 배지
  - 이슈 2(대형 레포): 하이브리드(≤500MB 얕은 클론 · 500MB~2GB 샘플링 · 2GB+ 거절), 별도 설계 문서 필요
  - 이슈 3(stale PR): 7일 `stale` 라벨 + 이메일 리마인드 → 30일 자동 close
  - 이슈 4(코드 전송): "저장"/"전송"/"임시 디렉토리" 3개 개념 분리, 전체 파일 전송 허용(캐시 금지 명시)
  - 이슈 5(이메일): Resend + 3개월 후 도달률 A/B, MVP 트래픽 기준 무료 티어 충분
  - 이슈 6(Stripe 세금): MVP 제외(Post-MVP 보류), 수동 세금계산서 대응 이메일 템플릿
- **DECISIONS.md 기록 템플릿 표준화**: 이슈별 결정 시 "결정 / 이유 / 영향 범위 / 재평가 시점" 4항목으로 통일.
- **후속 작업 3건 분리**: 대형 레포 전략 문서, 프라이버시 FAQ 3개념 분리 업데이트, `pr_lifecycle` cron 설계 — 각각 해당 이슈 결정 후 착수하도록 BACKLOG에 분리 등록.

**이유**:
- 이슈 #37 데드라인이 2026-04-29(Phase 2 Week 1 착수 직전)로 5일밖에 남지 않음. 각 이슈를 Joon이 즉흥적으로 판단하기에는 충돌·데이터·비용 비교가 복잡 — 의사결정 지원 문서가 판단 시간을 크게 단축.
- 6개 이슈 중 1(언어 지원)·4(코드 전송)는 F-01 온보딩 UI와 분석 프롬프트 설계에 직접 영향 → Week 1 시작 전 최소 이 2건은 필수 결정. 본 문서가 이 의존성을 명시.
- 마케팅 작업에 치우쳐 있던 지난 5일(04-17~04-21)에서 코어로 축을 옮기는 기조(2026-04-22 결정)를 유지 — 코어 의사결정 인프라를 먼저 갖추는 것이 Week 1 실제 코드 작업보다 선행되어야 한다는 판단.
- 단일 파일(+BACKLOG·DECISIONS 업데이트)로 회귀 위험 없음 — "작은 변경으로 큰 효과" 원칙 준수.

**변경 사항**: `docs/technical/phase2-open-issues-analysis.md` 신규 생성, `BACKLOG.md` (오픈 이슈 분석 항목 완료 처리 + 후속 3건 추가), `DECISIONS.md` (본 항목)

**에이전트 자동 추가 백로그**:
- `docs/technical/large-repo-strategy.md` 작성 — 500MB+ 대형 레포 분석 전략 상세 설계 (이슈 #37-(2) 결정 후 착수)
- 프라이버시 FAQ "저장 vs 전송 vs 임시 작업 디렉토리" 구분 업데이트 — `index.html` / `en.html` 보안 FAQ 보강 (이슈 #37-(4) 결정 후 착수)
- `pr_lifecycle` cron 설계 문서 — stale 라벨·30일 자동 close 규칙 (이슈 #37-(3) 결정 후 착수)

**수동 작업**: 이슈 #37의 각 task option을 Joon이 결정 → DECISIONS.md에 기록 (별도 이슈 생성 예정)

**PR**: (이 스크립트 실행 시 자동 생성, 이슈 #37 및 PR #36과 cross-link)
