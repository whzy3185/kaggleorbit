# Submit Confirmation: Official Starter Baseline

Date: 2026-06-16

This is a deliberate first submission to validate the official submission
contract and Kaggle feedback loop.

```yaml
competition_slug: orbit-wars
agent_name: official_starter_nearest_planet_sniper
package_path: main.py
source: data/official/main.py
package_size_bytes: 2079
package_sha256: 5253FA86A6191F3D718B8B9850E9D4AAF0BB2AA5E514E87D6B0FB40396DAEEFF
local_syntax_check: pass
local_tournament_check: not_run
manual_confirmation_source: user_requested_first_submission_before_targeted_build
known_risks:
  - starter baseline is weak
  - local environment smoke test is not verified yet
  - score is expected to be only a connectivity baseline
```

Exact command:

```powershell
kaggle competitions submit orbit-wars -f main.py -m "20260616_official_starter_connectivity_baseline"
```

Reason to submit:

- The account currently has no recorded submissions for `orbit-wars`.
- The official starter is the lowest-risk way to verify the live submission loop.
- Targeted agent work should start from a known official feedback baseline.

Reason not to over-interpret:

- This is not an optimized agent.
- Any score belongs to this starter baseline until later changes are submitted.
