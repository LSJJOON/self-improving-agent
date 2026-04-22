# MVP 최소 기능 명세서 (Functional Specification)

> **대상 독자**: ShipCrew MVP를 구현할 엔지니어(현재는 자율 에이전트 + Joon 본인).
> **전제 문서**: [`docs/technical/mvp-architecture.md`](./mvp-architecture.md) (기술 스택·아키텍처·데이터 모델·로드맵).
> **문서 목적**: 아키텍처를 "사용자가 실제로 쓰는 기능"으로 풀어서 명세한다. 각 기능마다 유저 스토리, 플로우, 수용 기준(Acceptance Criteria), 실패 처리, 계측 지표를 정의해 구현과 QA의 기준점을 만든다.

---

## 0. TL;DR

- **MVP 한 줄**: "1인 개발자가 GitHub 레포 1개를 연결하면, ShipCrew가 매일 한 번 자율적으로 개선 PR 1건을 생성하고 이메일로 요약을 보낸다."
- **MVP 스코프**: P0 기능 6개(연결·분석·PR·리포트·대시보드·결제). 각 기능은 본 문서에서 개별 명세.
- **출시 판정(Go/No-Go)**: §7의 6가지 기준을 모두 충족해야 런칭.
- **명시적 제외**: 멀티 레포, 팀 플랜, Slack/Discord, Self-hosted, 커스텀 모델 선택 — 모두 Post-MVP.

---

## 1. MVP 스코프 정의

### 1.1 포함(In Scope)

| 축 | 내용 |
| --- | --- |
| 지원 레포 수 | 계정당 **1개** 공개 또는 비공개 GitHub 레포 |
| 실행 주기 | **일간 1회**, 사용자 지정 시간(UTC 기준) ±30분 |
| 작업 단위 | 실행당 **PR 1건** (다중 커밋 가능, 단일 브랜치) |
| 언어/프레임워크 | **Python, JavaScript/TypeScript** 레포 우선 지원 (나머지는 Best-effort) |
| 과금 티어 | **Free**(공개 레포 1개, 주 1회) + **Pro $29/월**(비공개 포함, 매일) |
| 결제 | Stripe Checkout(구독), 카드만 — 세금계산서/수동송금 없음 |
| 알림 채널 | 이메일 1종(SendGrid or Resend) |
| 대시보드 | PR 이력 테이블, 다음 실행 시각, 구독 상태 — 3개 뷰 |

### 1.2 제외(Out of Scope, Post-MVP)

- 멀티 레포 동시 관리(Team 플랜 기능)
- Slack/Discord/Teams 연동
- Self-hosted / VPC 배포
- 커스텀 LLM 모델 선택(Claude 고정)
- 실행 결과 사람 검토 큐(Human-in-the-loop queue)
- 모바일 앱 / 푸시 알림
- GitHub Enterprise Server 지원

> **원칙**: 위 항목은 "하지 않는다"가 아니라 **MVP 출시 전까지 하지 않는다**. 수요 신호가 생기면 Post-MVP 백로그로 승격.

---

## 2. 사용자 여정(핵심 플로우)

```
(랜딩) → Waitlist 신청 → 초대 메일 수신
   ↓
(첫 로그인, GitHub OAuth) → 레포 1개 선택 → GitHub App 설치 승인
   ↓
(첫 실행 자동 트리거, 5분 내) → 첫 PR 생성 → 이메일 리포트 수신
   ↓
(다음 날부터 매일 1회 자동 실행)
   ↓
(첫 주 사용 후) → Pro 업그레이드 CTA → Stripe 결제 → 비공개 레포 활성화
```

목표 "처음 설치 → 첫 PR"까지 **5분 이내**. 이 지표는 §8의 North Star에 포함된다.

---

## 3. 핵심 기능 명세 (P0)

### F-01. GitHub App 설치 & 레포 연결

**유저 스토리**: "나는 GitHub OAuth로 로그인한 뒤 ShipCrew GitHub App을 설치해, 자율 에이전트가 작업할 레포 1개를 고른다."

**플로우**:
1. 사용자가 `shipcrew.dev/login` 에서 "Continue with GitHub" 클릭
2. GitHub OAuth 동의 → 프로필(email, avatar) 수집, Supabase Auth 세션 발급
3. "Connect your repo" 화면에서 "Install GitHub App" 버튼 → GitHub App 설치 페이지로 이동
4. 사용자가 대상 레포 1개 선택(계정 전체 허용 금지, **Selected repositories only** 강제)
5. 설치 완료 webhook 수신 → Supabase `installations` 테이블에 저장
6. 사용자에게 "연결됨 ✅ 첫 실행을 예약합니다" 메시지 노출

**권한(최소)**:
- Contents: Read & Write (PR 생성용)
- Pull requests: Read & Write
- Metadata: Read
- Issues: Read (컨텍스트 수집)
- **불가**: Actions, Secrets, Webhooks(레포), Admin

**수용 기준**:
- [ ] OAuth 로그인 성공률 ≥ 98% (실패 시 명확한 에러 메시지)
- [ ] 사용자가 여러 레포를 선택해도 UI는 1개만 "Active"로 표시
- [ ] 설치 취소(uninstall) webhook 수신 시 `installations.status = "revoked"`로 전환, 다음 실행 자동 중단
- [ ] 비공개 레포 연결 시 Free 사용자는 Pro 업그레이드 모달 노출(다운그레이드 선택지 포함)

**실패 처리**:
- OAuth 취소 → 로그인 페이지로 돌아가 "로그인이 필요합니다" 노출
- App 설치 취소 → 연결 단계 유지, 재시도 버튼
- 권한 부족 에러(403) → 권한 안내 도움말 링크 표시

**계측**:
- 이벤트: `oauth_success`, `app_install_success`, `repo_selected`
- 대시보드 지표: 설치 전환율 = `app_install_success` / `oauth_success`

---

### F-02. 레포 자율 분석(Agent Analysis)

**유저 스토리**: "내가 아무것도 하지 않아도, 에이전트가 내 레포를 읽고 오늘 할 만한 개선 작업 1건을 스스로 고른다."

**플로우**:
1. 스케줄러가 `installations.run_at`(사용자 지정 시각)에 Celery 태스크 enqueue
2. 워커가 GitHub App 토큰을 발급(설치별 단기 토큰)
3. `git clone --depth=50` 으로 최근 히스토리 포함 얕은 클론(임시 디렉토리)
4. 정적 스캔: `README`, `package.json` / `pyproject.toml`, `TODO/FIXME` 주석, `tests/` 커버리지 간이 측정
5. Claude API 호출 — 시스템 프롬프트에 "오늘의 1개 작업 제안" 지시 + 스캔 결과 요약 첨부
6. LLM이 **작업 후보 3개**를 JSON으로 반환 → 내부 스코어링 규칙(§3.2.1)으로 1개 선택
7. 선택된 작업을 `runs` 테이블에 저장 (`status="selected"`)

**3.2.1 작업 스코어링 규칙** (단순 가중치):
- `value_to_user`: 1~5 (에이전트 자가 평가)
- `scope_risk`: 1~5 (파일 변경 수 예상, 낮을수록 안전)
- `freshness`: 최근 동일 주제 PR 없을수록 높음
- 스코어 = `value_to_user * 2 − scope_risk + freshness`
- 동점 시 가장 작은 `scope_risk` 우선

**수용 기준**:
- [ ] 단일 실행의 종단간(end-to-end) 시간 **≤ 8분**(Claude API 호출 포함)
- [ ] 실패 시 재시도 1회 한정, 실패 로그는 Sentry + 본 `runs.error` 필드에 저장
- [ ] 최근 7일 내 동일 제목의 PR이 존재하면 해당 작업 후보는 자동 제외
- [ ] 임시 클론은 실행 종료 후 반드시 삭제(디스크 누수 0)

**실패 처리**:
- Clone 실패 → 다음 날 재시도, 사용자에게 "오늘 실행 실패" 이메일 1회 발송
- Claude API 429(Rate limit) → 지수 백오프 최대 3회, 이후 다음 날 재시도
- PR 후보 전원 탈락(스코어 음수 등) → "오늘은 건너뜀" 리포트 발송 + 다음 날 재시도

**계측**:
- 이벤트: `run_started`, `run_analyzed`, `run_candidate_selected`, `run_skipped`, `run_failed`
- 지표: 분석 성공률, 평균 실행 시간, 스킵 비율(5% 이하 목표)

---

### F-03. PR 생성

**유저 스토리**: "에이전트가 고른 작업에 대해 실제 코드 변경을 만들고, 내 레포에 PR을 올린다. PR 본문에는 왜 이 변경인지, 어떻게 테스트했는지가 적혀 있다."

**플로우**:
1. 선택된 작업을 Claude에게 다시 넘겨 **패치(diff) 생성** 지시
2. 생성된 diff를 임시 브랜치 `shipcrew/YYYY-MM-DD-slug`에 적용
3. 기존 테스트가 있으면 실행(타임아웃 3분) — 실패 시 LLM 자가 수정 1회
4. 변경 파일 수 > 15 또는 diff > 500 LOC면 **자동 축소**(가장 낮은 위험 영역만 남김)
5. GitHub API로 커밋 + PR 생성 (제목·본문·라벨 `shipcrew/agent`)
6. `runs.status = "pr_created"`, PR URL 저장

**PR 본문 템플릿**(§부록 A에 전문):
- `## 왜(Why)` — 작업 선택 이유, 레포 컨텍스트 근거
- `## 무엇(What)` — 변경 요약, 영향 파일
- `## 어떻게 테스트했는지(How Tested)` — 실행한 테스트 명령 + 결과
- `## 리스크/롤백` — 롤백 방법, 주의점
- `## 에이전트 메타` — 실행 ID, 선택된 후보 vs 탈락 후보 2개

**수용 기준**:
- [ ] PR은 항상 **새 브랜치**에 생성, `main` 직접 push 절대 금지
- [ ] 변경 LOC ≤ 500, 변경 파일 ≤ 15 (초과 시 자동 축소 또는 abort)
- [ ] 기존 테스트 전체 통과(테스트 없는 레포는 통과로 간주)
- [ ] PR 라벨 `shipcrew/agent` 및 `shipcrew/version=1.0` 자동 부착
- [ ] 7일간 머지되지 않은 PR은 자동 `stale` 코멘트 1회만(스팸 방지)

**실패 처리**:
- Diff 적용 실패(충돌) → Abort, 리포트에 "패치 충돌" 기재, runs.error 저장
- 테스트 실패(자가 수정 후에도) → PR을 Draft로 생성, 본문에 실패 로그 요약
- GitHub API 422(검증 실패) → 다음 날 재시도, 동일 제목 중복 방지 로직 활용

**계측**:
- 이벤트: `pr_created`, `pr_aborted`, `pr_test_passed`, `pr_test_failed`, `pr_merged` (webhook)
- 지표: PR 생성 성공률, PR 머지율(7/30일), 평균 LOC

---

### F-04. 일간 이메일 리포트

**유저 스토리**: "매일 아침 메일함을 열면 어제 밤 에이전트가 한 일이 한 눈에 보인다. PR 링크, 선택 이유, 다음 실행 시각."

**플로우**:
1. 실행 종료 시(성공·실패 무관) 리포트 레코드 생성
2. Resend(또는 SendGrid) API로 HTML + Plain 이메일 발송
3. 수신자: 레포 연결 계정 email + 사용자가 등록한 추가 수신자 1명(선택)
4. 이메일 내 CTA: "PR 보기 / 대시보드 / 설정 변경 / 일간 알림 끄기"

**이메일 섹션**:
- Hero: ✅ 오늘의 PR 1건 / ⏸ 오늘은 건너뜀 / ❌ 실행 실패
- 요약: 작업 제목, 선택 이유(2문장), PR 링크
- 테스트 결과: ✓/✗ + 실행한 명령 1줄
- 다음 실행: 예약 시각 + UTC→로컬 변환

**수용 기준**:
- [ ] 발송 성공률 ≥ 99% (bounce 제외)
- [ ] 스팸 분류 방지: SPF/DKIM/DMARC 정렬, `shipcrew.dev` 보낸사람
- [ ] 구독 해지 링크(unsubscribe) 본문 하단 필수 — List-Unsubscribe 헤더 포함
- [ ] 모바일(iPhone Mail, Gmail 앱)에서 단일 화면 내 요약 가독성

**실패 처리**:
- 이메일 전송 실패(bounce) → 대시보드 배너로 대체 알림, 3회 연속 실패 시 계정 이메일 확인 요청
- 사용자가 수신 거부 → 대시보드 전용 알림으로 전환(실행은 유지)

**계측**:
- 이벤트: `email_sent`, `email_opened`(픽셀), `email_clicked`, `email_unsubscribed`
- 지표: 오픈율(목표 ≥ 50%), CTR(목표 ≥ 30%)

---

### F-05. 결과 대시보드(Web)

**유저 스토리**: "에이전트가 지금까지 뭘 했는지 테이블로 보고 싶다. 설정도 이 한 곳에서 바꾼다."

**화면 구성(3개 뷰)**:

1. **Runs(기본 진입 페이지)**
   - 최근 30일 실행 이력 테이블: 일자 / 상태 / PR 링크 / 머지 여부 / 소요 시간
   - 각 행 클릭 → 상세(선택 사유, 후보 비교, 에러 로그)
   - 실행 수동 트리거 버튼(Pro 전용, 일간 1회 추가 허용)

2. **Repository**
   - 연결된 레포 정보, 설치 상태, 실행 시각, 언어 프로필
   - "레포 변경" / "연결 해제" 버튼

3. **Billing**
   - 현재 플랜(Free/Pro), 다음 청구일, 카드 4자리
   - "Pro 업그레이드" / "플랜 변경" / "결제 취소"(고객 포털 리다이렉트)

**수용 기준**:
- [ ] 모바일 360px 폭에서 테이블 가로 스크롤로 가독
- [ ] 인증 필수(미로그인 시 `/login` 리다이렉트)
- [ ] API P95 응답 < 500ms (Runs 30일치 기준)
- [ ] Playwright E2E: 로그인 → Runs 확인 → PR 링크 클릭 플로우 통과

**실패 처리**:
- API 오류 → 토스트 + 재시도 버튼
- 토큰 만료 → 로그인 페이지로 자동 리다이렉트(복귀 URL 유지)

**계측**:
- 페이지뷰, PR 링크 클릭, 수동 실행 클릭

---

### F-06. 결제 & 구독(Stripe)

**유저 스토리**: "비공개 레포를 연결하거나 매일 실행하려면 Pro로 업그레이드한다. 결제는 Stripe에 맡긴다."

**플로우**:
1. Free 사용자가 "비공개 레포 선택" 또는 "매일 실행" 시도 → Pro 업그레이드 모달
2. "Upgrade $29/mo" 클릭 → Stripe Checkout(구독) 세션 생성 → 결제
3. 웹훅(`checkout.session.completed`) 수신 → `subscriptions.status="active"`, `plan="pro"`
4. 이후 `invoice.paid` / `customer.subscription.deleted` 이벤트로 상태 동기화

**수용 기준**:
- [ ] 결제 성공 시 1초 내에 Pro 기능 활성화(웹훅 기반, 폴링 없음)
- [ ] 카드 정보는 ShipCrew DB에 저장 금지(Stripe 고객 포털 활용)
- [ ] 실패/환불 시 자동으로 Free로 강등, 경고 이메일 1회
- [ ] 부가세/세금계산서는 MVP 제외 — UI에 "영수증은 Stripe 고객 포털" 문구

**실패 처리**:
- 결제 실패 → Stripe 재시도 규칙 준수, 3회 실패 시 Pro 권한 회수 + 이메일 통보
- 웹훅 누락 → 매 15분 정기 recon job으로 Stripe 상태와 DB 정합성 보정

**계측**:
- 이벤트: `upgrade_modal_viewed`, `checkout_started`, `subscription_activated`, `subscription_canceled`
- 지표: Upgrade 전환율(waitlist→Pro), MRR, Churn

---

## 4. P1 기능 (출시 직후, 4주 내)

- Slack 알림 웹훅(1채널 단방향)
- GitHub Issue 자동 추출(TODO/FIXME → 백로그화)
- 사용자 지정 실행 시각 커스터마이징 UI(현재는 서버 기본값)
- 영어·한국어 i18n(랜딩은 이미 있음, 대시보드에 적용)
- "PR 머지율" 위젯

## 5. P2 (MVP+8주)

- 멀티 레포(Team 플랜 기준, 최대 10개)
- Claude 프롬프트 커스터마이징(사내 스타일 가이드 업로드)
- PR 템플릿 사용자 오버라이드
- Self-hosted Enterprise 옵션 검토(스펙만)

---

## 6. 비기능 요구사항(NFR)

| 항목 | 목표 |
| --- | --- |
| 가용성 | 월 99.0% (MVP, SLA 없음) |
| 일간 배치 완주율 | ≥ 95% |
| 평균 응답 속도(대시보드 API P95) | < 500ms |
| 일간 실행 시간 상한 | ≤ 10분/건 |
| 보안 | GitHub App 최소 권한, 토큰은 KMS 암호화 저장, PR 이력만 90일 보존 |
| 프라이버시 | 레포 코드 원본 저장 금지, Claude API 호출 시에도 캐시 비활성화 |
| 관측 | Sentry(에러) + Vercel Analytics + PostHog(프로덕트) |
| 비용 상한 | 월 서버비 $110 이하(Supabase + Railway + Resend 포함) |

---

## 7. 출시 판정 기준(Go/No-Go)

아래 6개를 **전부** 충족해야 런칭:

1. 실제 레포(에이전트 자신의 레포 + 테스트 레포 2개)로 7일 연속 무중단 실행 성공
2. 이메일 리포트 오픈율 ≥ 50% (내부 테스트 10명 기준)
3. 결제 플로우(Free → Pro) 종단간 10회 테스트 성공, 환불 1회 검증
4. 보안 체크리스트(OWASP Top 10 기본 + GitHub App 권한 감사) 통과
5. Playwright E2E: 온보딩·대시보드·결제 세 시나리오 통과
6. 개인정보/이용약관 페이지 공개 + 문의 이메일 작동

---

## 8. 지표 & North Star

- **North Star**: **주간 활성 에이전트 수**(= 해당 주 최소 1회 PR을 머지한 연결 레포 수)
- 보조 지표:
  - Time-to-First-PR(중앙값) ≤ 5분
  - 7일 Retention(D7, 2회 이상 실행) ≥ 70%
  - Pro 전환율(waitlist → Pro, 14일) ≥ 5%
  - MRR 목표(T+30일): $500
  - PR 머지율(30일 누계) ≥ 40%

---

## 9. 오픈 이슈(결정 필요)

1. **언어 지원 확장 시점** — MVP에서 Go/Rust 지원을 Best-effort로 둘지, 막을지?
2. **다이얼업 레포(매우 큰 레포)** — 500MB 이상 레포의 얕은 클론 전략은 별도 문서 필요
3. **"에이전트가 고장난 PR" 처리** — 7일 미머지 자동 close 정책 vs 사용자 선택권
4. **Free 플랜 제한** — "공개 레포 1개"인데 원격 서버에 코드 캐시 금지 시 어디까지 분석 가능한가(프롬프트에만 요약 첨부 vs 일부 파일 전송)
5. **이메일 공급자 선택** — Resend(개발자 친화) vs SendGrid(도달률 통계). MVP용 비용·도달률 A/B 필요
6. **Stripe 세금/인보이스** — 한국 사용자 세금계산서 요구 시 대응 방안(Post-MVP로 미뤄도 되는가)

각 이슈는 결정 즉시 DECISIONS.md에 기록.

---

## 10. 다음 단계(Phase 2 실행 순서)

1. **Week 1**: F-01(GitHub App + OAuth) 골격 — Next.js + Supabase Auth
2. **Week 2**: F-02(레포 분석) 프로토타입 — Celery + Claude API, 샘플 레포 2개로 E2E
3. **Week 3**: F-03(PR 생성) — 안전장치(LOC/파일 상한) 포함, 1주일 자가 dogfooding
4. **Week 4**: F-04 + F-05 — 이메일 리포트, 최소 대시보드 2뷰
5. **Week 5**: F-06 — Stripe 결제 전체 플로우
6. **Week 6**: 보안·E2E·성능 테스트, Go/No-Go 점검
7. **Week 7**: 얼리 어답터 10명 클로즈드 베타
8. **Week 8**: 공개 런칭(IndieHackers/ProductHunt)

---

## 부록 A. PR 본문 템플릿(초안)

```markdown
## 왜(Why)
{선택 이유 2~3문장. 예: "테스트 커버리지 보고에서 utils/ 디렉토리의 커버리지가 12%로 가장 낮았습니다. 작은 입력 검증 헬퍼부터 테스트를 추가해 빠른 안전망을 확보합니다."}

## 무엇(What)
- 영향 파일: `path/to/file.py` 외 N개
- 변경 요약: {한 문장}

## 어떻게 테스트했는지(How Tested)
```
$ pytest tests/utils
..... 12 passed in 0.8s
```

## 리스크/롤백
- 리스크: {없음/낮음/중간}
- 롤백: `git revert <sha>` 또는 본 PR을 close

## 에이전트 메타
- 실행 ID: `run_abc123`
- 선택된 후보: "utils/ 테스트 보강"
- 탈락 후보 1: "README 영문화" (낮은 freshness)
- 탈락 후보 2: "deps 업데이트" (scope_risk 4)

🤖 에이전트 자동 생성 PR — https://shipcrew.dev
```

---

## 부록 B. 용어 사전

- **Run**: 에이전트의 1회 실행 단위(하루 1건).
- **Candidate**: Claude가 제안한 작업 후보.
- **Installation**: GitHub App의 설치 인스턴스(레포 1개와 1:1).
- **Stale PR**: 7일간 머지되지 않은 에이전트 PR.
- **자가 수정(Self-heal)**: 테스트 실패 시 에이전트가 1회에 한해 패치를 보정.

---

**문서 버전**: 1.0 (2026-04-22, Phase 2 코어 우선 전환 첫 문서)
**다음 리뷰 시점**: F-01 구현 착수 직전(Phase 2 Week 1)
