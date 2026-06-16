# Optimization Direction Review

Date: 2026-06-16

This review converts the open-source/discussion audit into implementation
directions. It is not a Kaggle submission plan. The next work should remain
local until each change is benchmarked against public strategy families.

Structured candidates: `configs/next_optimization_candidates.yaml`.

## Evidence Used

- Official rules and replay access audit.
- 234 visible Kaggle discussion topics / 1,378 messages.
- 298 Kaggle Code entries and 27 pulled/static scanned notebooks.
- 103 GitHub repositories and 16 downloaded/static scanned repos.
- 9 public agents loaded locally; 8 match-smoked.
- 5 current high-rank visible replay samples from public episode datasets.
- Current profiler/counter coverage review.

## Highest-Value Directions

| Priority | Idea | Why now |
|---|---|---|
| P0 | Profile trace logging | Thresholds cannot be trusted until trigger timing is visible. |
| P0 | Fix `observed_turns` / confidence | Current accounting distorts turtle/low-send and trigger timing. |
| P0 | Opponent family benchmark pool | Every adaptive change needs repeatable public-family validation. |
| P0 | Recently captured recapture logic | Discussion and public code both indicate recapture windows matter. |
| P0 | Center/high-production control | Producer-style ROI and high-production targeting are under-countered. |

## Candidate Assessment

### 1. Fix observed_turns / confidence

The current profiler increments `observed_turns` per enemy-owned planet, not per
enemy per actual turn. This distorts low-send/turtle estimates and can inflate
confidence for successful expanders. Fixing this is low cost and should happen
before threshold tuning.

Expected gain: cleaner first-trigger timing and fewer false turtle/rush labels.

Risk: previous local thresholds may need retuning after the accounting change.

### 2. Profile trace logging

The audit found no evidence that current profile scores have been traced across
real matches against P0 public agents. Trace logging should record per-turn
scores, confidence, effective scores, selected modifiers, and supplemental
action counts under ignored `outputs/profile_traces/`.

Expected gain: converts profiler work from intuition to measurable behavior.

Risk: keep it optional to avoid runtime overhead.

### 3. Recently captured enemy planet recapture

Public discussion highlighted recapture shortly after ownership change as an
important behavior. Current code has generic counterattack bonus but no explicit
recent-capture state. Add ownership transition tracking and a target bonus for
low-garrison newly captured enemy planets.

Expected gain: punish overcommit and Producer-style capture floors.

Risk: over-focusing recapture can miss stronger expansion if transition scoring
is too aggressive.

### 4. Comet spawn timing preposition

Current comet logic is reactive: it detects observed comet targets and boosts
visible comet target scores. It does not model expected comet timing around
known windows or preposition ships before spawn. This should be P1 after trace
and baseline fixes because comet opportunities are phase-specific and easy to
overpay.

Expected gain: better comet contests and cleaner comet_greedy profiling.

Risk: bad lifetime valuation can waste ships.

### 5. Base-agent scoring injection

The current adaptive agent calls the base agent, then appends supplemental moves.
This is safe but weak; it cannot coordinate deeply with the base mission queue.
Injecting modifiers into the base scoring layer could improve recapture,
production denial, and enemy-specific pressure, but the blast radius is high.

Expected gain: stronger coordination with the selected Pilkwang base.

Risk: large public base code; change only after benchmark/trace harness exists.

### 6. 4-player threat prioritization

Public rules and replay samples confirm 4-player behavior matters. Current
counter policy reduces enemies by global max scores, so one enemy can change
behavior toward all opponents. Add per-enemy threat ranking using proximity,
production, fleet pressure, current strength, and attacks against us.

Expected gain: fewer wrong global reserve/attack reactions in 4P.

Risk: threat scores can oscillate without smoothing.

### 7. Anti-big-stack reinforcement and source counterattack

Public vkhydras lineage and high-rank samples show large sends and convergence
matter. The current counter only increases defense and counterattack bonuses.
Add explicit detection of depleted source planets, incoming stack size, and
defend-versus-evacuate choice.

Expected gain: better response to hammer/all-in attacks.

Risk: evacuation logic can throw valuable planets away if misfired.

### 8. Center/high-production planet control

The profiler computes `production_greedy` and `center_greedy`, but counter policy
does not consume either. This is a direct gap against Producer-style and
high-production opening behavior. First activate production denial; center should
remain gated by production/ETA because replay evidence for pure center control
is weaker.

Expected gain: better denial of production-positive targets.

Risk: overvaluing center geometry when production is low.

### 9. Profile-specific reserve floor

Current reserve changes are global. A distant rusher or conflict targeter can
raise reserve everywhere. Use profile-specific threat proximity so only relevant
own planets reserve more ships.

Expected gain: more available ships in 4P while maintaining defense.

Risk: implementation complexity; lower priority than trace and benchmark.

### 10. Opponent family benchmark pool

The Stage 5 public pool makes this practical. Define small benchmark groups by
strategy family: starter/nearest, Producer-style, distance pressure, defensive
reinforce, big-stack, hybrid layered, and ML/RL-like. Use fixed seeds and
bidirectional schedules, then store local-only outputs under ignored `outputs/`.

Expected gain: prevents blind optimization and catches regressions by family.

Risk: public-pool overfit; label all results as local-only.

### 11. weak_bot / starter-like bot recognition

`weak_bot` is currently dead. Implement a low-risk weak/starter profile that
detects simple nearest expansion, poor production targeting, missing defense,
and low multi-source behavior. The counter should expand greedily, not blindly
all-in.

Expected gain: faster conversion versus weak public/starter bots.

Risk: false positives against slow strong agents.

### 12. Gold/high-rank replay feature extraction

Final gold teams do not exist yet as of 2026-06-16, so no gold strategy claims
should be made. Current high-rank replays are visible through public episode
datasets and can be sampled. Expand feature extraction carefully and keep raw
features ignored.

Expected gain: empirical priors for opening, first attack, defense, comet, and
commit ratios.

Risk: daily datasets can be huge; sample intentionally.

## Recommended Next Step

Start with `profile_trace_logging`, then immediately fix `observed_turns` /
confidence and run the same trace harness again. This gives before/after evidence
for the profiler before any counter behavior becomes more aggressive.

The first code task should not change strategic behavior by default. It should
only add optional local trace output and a repeatable public-family benchmark
entrypoint.
