# Public Output Source Recheck

Date: 2026-06-17

Purpose: answer whether the current Vkhydras Last submission is definitely the
highest-value public base. It is not.

## Direct Answer

No. The current repository had pulled and scanned many public notebooks, but
the selected Vkhydras Last base was only the best completed official submission
from our workspace at that moment. It was not verified as the highest-scoring
public/open-source model or package.

The user's package-size concern was valid as an audit trigger. Package size is
not a score guarantee, but it exposed a real gap: several high-signal Kaggle
outputs were not loaded into the local benchmark pool before targeted V1 work
continued.

## Current Vkhydras Package

```yaml
dist_main_py_bytes: 286646
vkhydras_last_source_bytes: 294677
pilkwang_source_bytes: 106245
current_official_workspace_best:
  agent: vkhydras_last_heuristic
  submission_id: 53772607
  latest_observed_public_score: 810.6
```

This is a light single-file heuristic package. It is not an original model and
not a learned-weight package.

## Fresh Kaggle Code Recheck

`kaggle kernels list --competition orbit-wars --sort-by scoreDescending` showed
several high-signal entries that were not in the loaded local public pool:

- `ranjeet258/orbit-wars-producer`
- `romantamrazov/orbit-wars-i-m-stronger`
- `alycemiki/light-ver-1200-simple-orbit-intruder`
- `caoyupeng/v2-gru`
- `shummingfang/orbit-wars-exp50`
- `reyhanksatria/orbit-wars-reyhan-ksatria`
- `mirzayasirabdullah07/best-orbit-wars-notebook`
- `jek1wantaufik/orbit-wars-submission-build-and-testing`
- `jek1wantaufik/simplified-orbit-wars-agent`
- `alycemiki/intervention-command-w-ffa`

Their source notebooks and outputs were downloaded to ignored local paths:

```text
external/kaggle_notebooks/
external/kaggle_outputs/
```

These files are not committed.

## Output Package Structure

Most of the fresh outputs are multi-file `submission.tar.gz` packages using an
`orbit_lite` package and `torch`.

Typical package sizes:

| Output | tar.gz bytes | unpacked bytes | Notes |
|---|---:|---:|---|
| `ranjeet258/orbit-wars-producer` | 55,220 | 208,509 | `main.py` + `orbit_lite/` |
| `romantamrazov/orbit-wars-i-m-stronger` | 54,902 | 208,442 | `main.py` + `orbit_lite/` |
| `alycemiki/light-ver-1200-simple-orbit-intruder` | 55,051 | 210,371 | `main.py` + `orbit_lite/` |
| `caoyupeng/v2-gru` | 56,487 | 217,691 | `main.py` + `orbit_lite/` |
| `shummingfang/orbit-wars-exp50` | 52,898 | 205,190 | `main.py` + `orbit_lite/` |

The public outputs pulled here are not 70x larger than `dist/main.py`; they are
actually smaller as compressed tarballs and similar after unpacking. If a
70x-larger package is visible elsewhere, it likely includes additional
artifacts, private assets, or a different model/package that is not represented
by these public outputs.

## Smoke Results

After fixing `scripts/smoke_single_file_agent.py` to register dynamically loaded
modules in `sys.modules`, all 10 fresh output agents loaded and ran a smoke
match against random with `env_status: ok`.

## Minimal Local Screen Against Vkhydras Last

Local-only screen: 3 seeds, bidirectional, fast runner.

| Candidate | Result vs `vkhydras_last_heuristic` | Errors |
|---|---:|---:|
| `ranjeet258/orbit-wars-producer` output | 6-0 | 0 |
| `romantamrazov/orbit-wars-i-m-stronger` output | 6-0 | 0 |
| `alycemiki/light-ver-1200-simple-orbit-intruder` output | 6-0 | 0 |
| `caoyupeng/v2-gru` output | 5-1 | 0 |
| `shummingfang/orbit-wars-exp50` output | 6-0 | 0 |

This is a small local screen, not an official score. Still, it is strong enough
to reject the assumption that Vkhydras Last is the best local base.

## Targeted V1 Context

The conservative targeted V1 candidate also failed its first local
non-regression check:

```yaml
vkhydras_last_base_vs_targeted_v1:
  seeds: 10
  bidirectional: true
  base_wins: 15
  targeted_wins: 5
  errors: 0
```

That result reinforces the same decision: stop tuning targeted filters on
Vkhydras until the base is reselected.

## Recommendation

Do not continue Vkhydras-targeted optimization as the main line.

Next work should be:

1. Promote the fresh public output packages into an ignored local benchmark
   pool.
2. Run a larger 2P and 4P screen among:
   - `ranjeet258/orbit-wars-producer`
   - `romantamrazov/orbit-wars-i-m-stronger`
   - `alycemiki/light-ver-1200-simple-orbit-intruder`
   - `caoyupeng/v2-gru`
   - `shummingfang/orbit-wars-exp50`
   - `vkhydras_last_heuristic`
   - previous P0 pool
3. Select a new base from the public output winners.
4. Only then redesign targeted logic around that new base.
5. Do not submit Kaggle until a new package audit and confirmation card exist.
