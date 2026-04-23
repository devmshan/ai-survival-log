# Blog Draft Review Rules

## Purpose

This document defines the two-axis review rules for publishable wiki pages and their derived MDX blog drafts in `ai-survival-log`.

Two axes that existing review tools do not cover:

- **Axis A — Source Fidelity**: faithfulness of the draft to the raw journal or source material
- **Axis B — Writing Craft**: sentence-level quality, tone, and readability

This document is applied before `/wiki:publish`, after authoring is substantially complete.

## Scope Boundary

Applies to:

- `output/blog/*.mdx` and their source `wiki/topics/*.md` pages

Does not apply to:

- `raw/` originals
- `wiki/sources/` summaries
- `wiki/entities/` and `wiki/concepts/` definition pages
- YouTube scripts, carousels, or other non-blog lanes

Those lanes may reuse principles from this document, but they need their own lane-specific contract once they become official workflows.

---

## Why This Exists

The existing `/content:review-blog-draft` 7-item check covers narrative structure (headers, WHY, section motivation, depth, noise, arc, scope).

Two gaps remain:

1. **Source Fidelity**: Does the draft stay faithful to raw journals and named sources? Are proper nouns grounded? Are external frames labeled as external?
2. **Writing Craft**: Does the draft use one anchor per post? Are anti-patterns (triple negation, triple nesting, abstraction spikes, repeated definitions from earlier posts) absent?

This document was created after a 2-agent cross-review of four posts published on 2026-04-24. Concrete failure and fix examples below are drawn from that review.

---

## Core Principles

- Claims not in the source do not appear in the draft.
- Assertions are softened to match source confidence level.
- Each post has one anchor sentence.
- Definitions established in an earlier linked post are not re-explained.
- One concept uses one vocabulary word throughout.
- Abstraction rises one level at a time.

## Enforcement Levels

### `warn`

- Original evidence is weak but intent is intact — fix by softening the assertion
- Vocabulary drift (e.g., 도망길 / 길 / 방향 mixed in the same post) — fix by picking one
- Sentence-ending repetition ("~하는 구조다" 3+ times in one section) — fix by rewording
- Translation-style phrasing ("~에 대한", "~를 통해서") 2 occurrences or fewer

### `block`

- A proper noun or numeric claim appears in the draft but has no grounding in `raw/journals/` or a named external source — do not publish until generalized or sourced
- An externally borrowed frame is written as if self-originated — do not publish until source attribution is added
- A definition from an earlier linked or series post is re-explained in full — do not publish until replaced with link + 1-line summary
- Two or more anchor-level sentences compete in the same post — do not publish until one is weakened
- Triple negation pattern ("~가 아니다. ~도 아니다. ~도 아니다.") — do not publish until compressed to one sentence
- Triple nesting in a closing sentence ("A 쌓이면 B, B 쌓이면 C, C 쌓이면 D") — do not publish until reduced to two levels

### `escalate`

- Changing a shared anchor sentence that appears across multiple posts
- Adjusting MUST / SHOULD / MAY enforcement grades in this document
- Expanding Axis A or Axis B scope to cover other lanes (YouTube, carousel, etc.)

---

## Axis A — Source Fidelity

Agent 1 in the standard 2-agent cross-review performs this axis.

### MUST

**1. Proper nouns must be grounded in source material.**

Any proper noun (model name, product name, number) introduced in the draft must appear in `raw/journals/` or a named external source. If it is absent from the source, generalize.

- fail: `"Evo 2, AlphaGenome 같은 모델들이…"` — these names do not appear in the source journal → `block`
- fix: `"최근 유전체·단백질 분야에서 나오는 대형 모델들이…"`

**2. Externally borrowed frames must be labeled as external.**

A concept taken from an external podcast, article, or secondary source must include attribution. Do not write it as if it is a self-originated idea.

- fail: opening line `"두 갈래 도망길이 있다"` with no attribution → `block`
- fix: `"두 갈래 도망길이 있다는 이야기를 들었다. 팟캐스트와 외부 아티클에서 나온 프레임이었다."`

**3. Assertions are softened to match source confidence.**

When the raw journal records a user impression, feeling, or hypothesis, the draft must reflect the same level of certainty. Do not convert impressions into facts.

- fail: `"Anthropic이 tokenizer를 바꿨다"` — journal records only a user impression → `warn`
- fix: `"tokenizer 설계가 달라진 것 같다는 체감이 있었다"`

**4. User-originated insights must be preserved as user-originated.**

When the raw journal shows the user as the originator of a metaphor, question, or conclusion, the draft must preserve that attribution. Do not rewrite it as assistant explanation.

Each post should contain at least one marker sentence or block quote that makes user authorship clear.

### SHOULD

- Before writing each section, map it to the corresponding raw journal line range. Note the mapping in the writing plan.
- When quoting an anchor sentence verbatim from the source, preserve the exact wording.
- Key signal passages from the journal (conclusion scenes, turning-point questions) should be preserved unless there is an explicit reason to trim them.
- In a series, refer back to definitions and anchor sentences already established in earlier posts rather than redefining them.

### MAY

- Add one sentence of clarifying context that does not contradict the source.
- Retain a proper noun if a separate source attribution is added inline and the assertion is softened.

### Axis A Review Checklist

1. Extract the section structure of the target MDX.
2. Map each section to a raw journal line range. Any section without a mapping is an Axis A failure candidate.
3. Grep all proper nouns in the draft against `raw/` to verify grounding.
4. Check that each externally borrowed concept frame has an attribution sentence in the draft.
5. Confirm that key conclusion or turning-point passages from the journal are present or intentionally cut.

---

## Axis B — Writing Craft

Agent 2 in the standard 2-agent cross-review performs this axis.

### Tone Baseline

Reference post: `wiki/topics/how-llm-works.md`

Default style: first person, short sentences, "근데 / 그래서" transitions, minimal definition-heavy statements, narrative section headers.

### MUST

**1. One anchor per post.**

The closing section must not produce a second anchor sentence that competes with the first. If two sentences read as equally strong conclusions, weaken one.

- fail: 03편 — both `"루프를 닫을 수 있는 영역 = 평가 가능한 영역이다"` and `"생성과 검토가 같은 시스템 안에 있는가"` carry equal conclusion weight → `block`
- fix: reduce the earlier sentence to `"루프를 닫을 수 있는 곳에는 반드시 평가 기준이 있다."` (one tone lower)

**2. No triple negation.**

The pattern "~가 아니다. ~도 아니다. ~도 아니다." must be compressed to one sentence.

- fail: `"하네스는 agent를 여러 개 두는 것이 아니다. brain과 hand를 나누는 것만도 아니다. 개인과 회사 도메인을 분리하는 것만도 아니다."`
- fix: `"하네스는 agent 수를 늘리거나 도메인 경계를 선언하는 것만으로 완성되지 않는다."`

**3. No triple nesting in a closing sentence.**

The pattern "A 쌓이면 B, B 쌓이면 C, C 쌓이면 D" must be reduced to two levels.

- fail: `"선택이 쌓이면 취향이 되고, 취향이 쌓이면 나의 출력이 되고, 나의 출력이 나의 흔적이 된다."`
- fix: `"선택이 쌓이면 취향이 되고, 취향이 쌓이면 나의 출력이 된다."`

**4. No re-explanation of definitions from earlier linked posts.**

When a post is part of a series or cross-links to an earlier post that defined a concept, do not re-explain that concept in full. Replace with a link and a 1-line summary.

- fail: 04편 re-explains the full LM head / parameter / hidden state definition already established in 02편 → `block`
- fix: `"02편에서 정리한 LLM 구조와 맞대어 보면 이상하게 맞아떨어진다. 파라미터는 학습된 가중치, hidden state는 중간값, LM head는 출력층이다."` (1-line summary + link)

**5. No abstraction spike without an immediate concrete example.**

When an abstract term or category is introduced, the same section must provide at least one concrete example one level down before rising further.

- fail: 글3 — introduces "프로젝트는 결과물, 계약, 권한 경계 기준으로 나눈다" and immediately names Planning / Review / Engineering lane types, with no grounding example → `block`
- fix: `"블로그 집필, 회사 기획, 코드 작업은 각각 다른 저장소와 승인 구조를 가진다. Planning, Review, Engineering 같은 역할은 이 경계를 가로질러 재사용된다. 블로그 기획도 Planning이고, 회사 보고서 기획도 Planning이다."`

### SHOULD

- **Avoid translation-style phrasing.** Minimize "~에 대한", "~를 통해서", "~하는 것이다". Aim for 3 or fewer per post.
- **Diversify sentence endings.** The same ending ("~하는 구조다") should not repeat 3 or more times within one section.
- **Vocabulary unification.** One concept uses one word. If "도망길 / 길 / 방향 / 경로" are used interchangeably, pick one and apply it throughout.
- **Compress hypothesis-negation-explanation arcs.** When the source journal uses three steps (hypothesis → negation → explanation), compress to two in the draft (hypothesis → why it was wrong).
- **Block quote economy.** Use 1–2 block quotes per post, only at genuine turning points.
- **Active-voice subjects.** Before finalizing, scan for passive or subject-dropped constructions and convert at least once to a first-person active form.

### MAY

- Repeat shared transition phrases (근데, 그래서, 그리고) across posts published the same day — this signals series continuity to the reader.
- Keep technical terms (LM head, hidden state, etc.) in English or add a Korean gloss — either is acceptable.

### Axis B Review Checklist

1. Read the target MDX alongside `wiki/topics/how-llm-works.md` and compare tone.
2. Extract the last sentence of each section as anchor candidates. If two or more read as equal-strength conclusions, reduce one.
3. Scan for: "~가 아니다" three times in a row, "~쌓이면" three times in a row, "~하는 구조다" three or more times in one section.
4. Open any earlier post that is linked or series-connected. Check whether any of its definitions are re-explained in full in the current draft.
5. In each section that introduces an abstract term, verify that a concrete example follows within the same section.

---

## Review Procedure — Standard 2-Agent Cross-Review

Perform this procedure before `/wiki:publish` or before final content sign-off.

### Step 1. Prepare targets

- Confirm the list of MDX files to review.
- Confirm the corresponding `wiki/topics/*.md` pairs.
- For each post, collect the raw journal line ranges that correspond to each section.

### Step 2. Launch two agents in parallel (single message, two Agent tool calls)

**Agent 1 — Axis A (Source Fidelity)**

- Input: list of target MDX files + corresponding `raw/journals/` line ranges
- Task: run the Axis A MUST and SHOULD checklist; grep all proper nouns against `raw/`; confirm external frame attribution; assess assertion strength
- Output: per-file violation list with line number, enforcement level (block / warn), and a fix suggestion

**Agent 2 — Axis B (Writing Craft)**

- Input: list of target MDX files + tone baseline file `wiki/topics/how-llm-works.md`
- Task: run the Axis B MUST and SHOULD checklist; detect anchor competition, triple negation, triple nesting, abstraction spikes, translation-style phrasing
- Output: per-file violation list with line number, enforcement level, and a fix suggestion

### Step 3. Triage and edit

Prioritize in three tiers:

1. **Block level** (highest priority): Axis A MUST violations, anchor competition, abstraction spikes
2. **Warn level**: assertion softening, external source attribution, narrative bridge gaps
3. **Style level**: vocabulary unification, translation-style phrasing, repetition patterns

Edit `wiki/topics` and `output/blog` as pairs. Never update one without the other.

### Step 4. Re-verify

- Run `/wiki:lint` — wikilink integrity.
- Run `/content:review-blog-draft` — all 9 items (original 7 + Axis A/B items 8 and 9).
- Self-check `docs/publishing-contract.md` and `docs/content-seo-guide.md`.

### Step 5. Publish

When all checks pass, proceed with `/wiki:publish`.

---

## Integration with `/content:review-blog-draft`

This document extends the review command with two additional checklist items:

| Item | Name | Verification question |
|---|---|---|
| 8 | **Source Fidelity (Axis A)** | Are proper nouns, assertions, and external frames grounded in the source? Is user-originated authorship preserved? |
| 9 | **Writing Craft (Axis B)** | Is there one anchor? Are triple negation, triple nesting, repeated definitions, and abstraction spikes absent? |

Axis A and B `block`-level violations map to `FAIL`. `warn`-level violations map to `WARN`.

---

## Maintenance

- When adding new enforcement rules, prefer raising an existing SHOULD to MUST before adding a new MUST. The total MUST count across both axes should stay at or below 10.
- When publishing rules change, re-check this document together with `docs/publishing-contract.md` and `docs/content-seo-guide.md`.
- When new failure patterns emerge from future multi-post reviews, add concrete fail / fix examples to the relevant MUST item.
