# Launch Posts — 얼리 어답터 모집 콘텐츠 초안

> 작성일: 2026-04-21
> 목적: ShipCrew 랜딩 페이지(https://shipcrew.dev) 준비 완료 후 IndieHackers, ProductHunt, Twitter/X 등 주요 채널에 게시할 런칭 포스트 초안.
> 한국어·영어 버전 모두 포함. 실제 게시 전 최종 카피 리뷰 필요.

---

## 1. IndieHackers 포스트 (영문)

### 제목 후보
1. **I built an agent that ships a PR to my SaaS every morning — waitlist open**
2. What if your side project could grow while you sleep? (Building ShipCrew)
3. Devin is $500/mo. I'm building a 1/17-price alternative for solo devs.

**권장**: #1 — 구체적·개인적·호기심 유발 (IndieHackers 첫 문장이 피드 클릭률을 결정)

### 본문 (영문, 약 350 단어)

Hey IndieHackers,

For the past six months I've watched the same pattern repeat on my own side projects: push hard for two weeks, ship the skeleton, then watch the daily grind of features + support + marketing drown the project before it can reach traction. I've killed two side SaaS projects this way.

So I asked a different question: what if my project could ship one useful PR every single day, even when I'm exhausted, traveling, or just off the grid?

That's what I've been building for the last 30 days. It's called **ShipCrew**.

**How it works**

- Connect a GitHub repo.
- Every morning the agent reads your `BACKLOG.md`, picks the highest-value task, and ships a PR with a short decision log.
- You review, merge (or close), and your project moves forward every day.

It's not another IDE copilot. It's closer to a junior teammate who never sleeps, never quits, and writes down its reasoning so you can audit every choice.

**Why I think this is different**

1. **Price** — Devin runs around $500/mo and is aimed at enterprise. ShipCrew is aimed at indie devs at **$29/mo**.
2. **Transparency** — every decision is logged in `DECISIONS.md` you can read line by line. No black box.
3. **Dogfooded in public** — the agent ships PRs to its own repo every day. You can watch it operate live: github.com/LSJJOON/self-improving-agent

**Landing page + waitlist**: https://shipcrew.dev

**What I'd love your take on**

- What kind of task would you trust an agent to ship unsupervised on your repo?
- What kind of task would you never let it touch?
- If the answer to #1 is "none," what would the agent have to prove first?

I'll answer every reply in this thread. Thanks for reading.

— Joon

---

## 2. ProductHunt 런칭 페이지 초안 (영문)

### Tagline (60자 이내 권장)

`Your side project ships a PR every morning — while you sleep.`

### Description (260자 이내)

ShipCrew is a GitHub-connected agent for solo devs. Every morning it picks the highest-value task from your backlog, ships a PR, and logs its reasoning — so your product grows even on the days you can't. Built for indie pricing. Full decision transparency.

### Topics (권장)

- Developer Tools
- Artificial Intelligence
- GitHub
- SaaS
- No-Code (해당 시)

### Maker's first comment (런칭 당일 engagement의 핵심)

Hey Hunters 👋

I'm Joon, a solo dev who has killed more side projects than I want to count — always for the same reason: the excitement of week 1 never survives the grind of month 3.

ShipCrew is my attempt to fix that at the only point that's actually fixable: the day itself.

**What the agent does**

- reads your backlog every morning
- picks the task most likely to move the product forward
- ships a PR you can review, merge, or reject
- writes a human-readable decision log for every choice it makes

**What I'd love PH feedback on**

1. Does "a teammate who ships 1 PR/day" resonate, or does it feel too narrow?
2. At $29/mo, what would you need to see working on a real repo before you'd trust it?
3. What's the first kind of task you'd assign it — and the first kind you'd keep to yourself?

Landing + waitlist: https://shipcrew.dev · repo: github.com/LSJJOON/self-improving-agent

I'll be here all day — AMA.

---

## 3. Twitter/X 런칭 스레드 (영문, 7 tweets)

**Tweet 1 (hook)**

Today I'm opening the waitlist for a thing I've wanted for a year:

an agent that wakes up every morning, opens my SaaS repo, picks the most valuable task, and ships a PR — before I pour coffee.

It's called ShipCrew. Quick thread 🧵

**Tweet 2 (problem)**

The solo-dev death spiral:
• week 1 — "new project!"
• week 2 — "still shipping!"
• week 5 — "I'll get back to it tomorrow"
• week 12 — repo is dead

Every indie dev I know has lost projects this way. Momentum is the only thing that matters and the hardest thing to keep.

**Tweet 3 (solution)**

ShipCrew fixes this at the only point that's actually fixable: **the day itself.**

Every day it ships 1 PR.
Every PR includes a written rationale.
You approve, merge, or reject.

After 30 days you have 30 PRs of forward progress — not 30 days of silence.

**Tweet 4 (dogfooding)**

I'm dogfooding it on its own repo.

It picked today's task, wrote the code, opened the PR, and updated its own backlog — while I slept.

Public receipts: github.com/LSJJOON/self-improving-agent

**Tweet 5 (pricing)**

Pricing:
• Free — 1 public repo, weekly
• Pro — $29/mo, 5 repos, daily
• Team — $79/mo, unlimited

Devin runs around $500/mo. Cursor is IDE-scoped.
ShipCrew is aimed at the part of your day when you're not at the keyboard.

**Tweet 6 (bet)**

Three bets behind this:
1. A written decision log every day — no black-box AI.
2. Pricing an indie dev can actually justify.
3. Focused scope: one PR per day, shipped, reviewed, merged. Not a thousand suggestions.

**Tweet 7 (CTA)**

Waitlist is open: https://shipcrew.dev

Early access will be invite-only so I can tune per-repo behavior.

Would love to hear: what's the first task you'd trust an agent to ship on your repo — and what would you never let it touch?

---

## 4. 한국어 버전 (F-Lab, 요즘IT, 디스콰이엇, 네이버 카페 등 국내 인디 커뮤니티)

### 제목 후보

1. **자는 동안 매일 PR이 하나씩 쌓이는 SaaS를 만들고 있습니다 — 얼리 어답터 모집**
2. 사이드 프로젝트가 죽는 이유를 해결하는 제품(ShipCrew) waitlist 오픈했습니다
3. Devin 월 $500 대신, 월 $29로 "매일 1PR" — 인디 개발자용 자율 코드 에이전트

### 본문

안녕하세요, Joon입니다.

사이드 프로젝트를 해보신 분이라면 이 패턴을 아실 겁니다. 1주차에는 몰입해서 푸시하고, 5주차에는 "내일 해야지"가 되고, 12주차에는 레포가 조용해집니다. 저도 이렇게 사이드 SaaS 두 개를 묻었습니다.

문제는 의지나 시간이 아니라 **매일 조금씩 전진하는 구조**가 없다는 것이었습니다. 그래서 만들고 있는 제품이 **ShipCrew**입니다.

**어떻게 동작하나요?**

- GitHub 레포를 연결합니다.
- 매일 아침 에이전트가 `BACKLOG.md`에서 가장 가치 있는 작업 1개를 골라 PR을 생성합니다.
- 모든 의사결정은 `DECISIONS.md`에 한국어로 기록됩니다.
- 머지하거나 닫으면 됩니다 — 다음 날 또 1개의 PR.

30일 뒤에는 PR 30개만큼 전진해 있습니다. "잠든 사이 제품이 자랍니다."

**Devin·Copilot과 뭐가 다른가요?**

- Devin은 월 $500대 가격. ShipCrew Pro는 월 $29 (약 1/17).
- 모든 의사결정이 텍스트로 로깅됨 — 블랙박스 없음.
- 제품 자체가 자기 레포에 매일 PR을 만들면서 개발 중 — 실시간 공개 증명.

**얼리 어답터를 찾습니다**

- 랜딩 페이지 + waitlist: https://shipcrew.dev
- 실시간 개발 과정 공개 레포: github.com/LSJJOON/self-improving-agent
- 베타는 레포 특성별로 튜닝하기 위해 소수에게 순차 초대 예정입니다.

**피드백 환영합니다**

- 어떤 작업이라면 에이전트에게 PR을 맡기실 건가요?
- 어떤 작업은 절대 맡기지 않으시겠어요?
- `$29/월`이 합리적으로 느껴지시나요, 비싸게 느껴지시나요?

감사합니다.

— Joon

---

## 5. 채널별 게시 전 체크리스트

- [ ] 랜딩 페이지 Vercel 배포 상태 확인 (shipcrew.dev 200 OK)
- [ ] waitlist 폼이 Formspree로 실제 수집되는지 이메일 2건 수동 테스트
- [ ] og-image.png 1200x630 이미지 실제 파일 업로드 — 현재 경로만 참조됨 (백로그 항목)
- [ ] IndieHackers 계정 프로필에 shipcrew.dev 링크
- [ ] ProductHunt 런칭은 화요일/수요일 UTC 00:01 목표 (주간 랭킹 기회 최대화)
- [ ] Twitter 스레드 예약 시각 UTC 14:00 권장 (US East 오전 출근 시간)
- [ ] UTM 파라미터 적용 — PR #32(UTM 추적) 머지 후 채널별 URL 생성
  - IndieHackers: `?utm_source=indiehackers&utm_medium=post&utm_campaign=launch_2026q2`
  - ProductHunt: `?utm_source=producthunt&utm_medium=launch&utm_campaign=launch_2026q2`
  - Twitter: `?utm_source=twitter&utm_medium=thread&utm_campaign=launch_2026q2`
- [ ] GA4 실시간 대시보드 오픈 (런칭일 ±48시간 관찰)

---

## 6. 게시 후 대응 가이드

**24시간 룰**: ProductHunt와 IndieHackers는 첫 24시간의 engagement가 랭킹을 거의 결정합니다. 런칭 당일은 다른 일정을 비워두고 모든 댓글에 30분 내 답장.

**FAQ 질문 처리**: 반복 질문은 `shipcrew.dev/#faq` 앵커로 유도 (신뢰 신호 누적).

**부정 피드백 대응**: 비판이 타당하면 24시간 내 DECISIONS.md에 해당 결정 공개 수정 — "매일 투명하게 개선하는 팀" 포지셔닝 강화.

**초기 목표 수치 (참고용)**

- 런칭 당일 waitlist: 100명
- 3일 누적: 300명
- 1주 누적: 500명
- PH Product of the Day Top 5 진입 목표

실제 수치는 GA4 + Formspree 대시보드에서 일별 추적.

---

## 7. 다음 단계

1. **UTM 파라미터 (PR #32)** 머지 → 채널별 URL 실제 생성.
2. **og-image.png** 디자인 및 업로드 → SNS 공유 시 시각 카드 완성.
3. **사용 데모 GIF** 제작 → 랜딩 페이지 + 런칭 포스트에 삽입 (전환율 +)
4. **디스콰이엇·인프런 인사이트 콘텐츠** 별도 포스트 작성 (한국 1인 개발자 커뮤니티 심화 공략).

---

이 문서는 **초안**입니다. 실제 게시 전:
- Hero 카피(`landing-page-copy.md`)와의 문구 일관성 재검토
- Formspree/GA4 동작 테스트
- og-image + UTM 준비 완료 확인

가 반드시 선행되어야 합니다.
