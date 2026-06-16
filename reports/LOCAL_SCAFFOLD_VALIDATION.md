# Local Scaffold Validation

Date: 2026-06-16

Validation commands:

```powershell
python scripts\smoke_adaptive_agent.py
```

Result:

```text
[[0, 0.14189705460416394, 9]]
```

Additional compile check:

```powershell
$files = Get-ChildItem -Path src\orbitwars_agent, agents\adaptive_agent, scripts -Filter *.py -File -Recurse | ForEach-Object { $_.FullName }
python -m py_compile @files
```

Result: pass.

Public tooling:

- `external/orbit-wars-lab` was cloned successfully.
- It is ignored by git through `external/`.
- README indicates 11 bundled agents and local tournament support.

Submission decision:

- Do not submit `agents/adaptive_agent/main.py` yet.
- It is only a scaffold until evaluated against public agents in a tournament.

