Last Edit: Codex - 2026-10-25 - Motive: Record compatibility-fork package metadata.

# Quick Facts

| Property | Value |
| --- | --- |
| Package | `combo_lock` |
| Version | `0.3.1+thalovant.1` |
| Python | >=3.10 |
| Entry points | None declared |
| API | `ComboLock`, `NamedLock` in [combo_lock/combo_lock.py](combo_lock/combo_lock.py) |
| Python 3.10 dependency | `filelock==3.20.3` |
| Python >=3.11 dependency | `filelock>=4.2.1,<5` |
| Publication | Fork PR only; no PyPI release |

The real installation requirements come from `requirements.txt` through
`pyproject.toml`. [Evidence and caveats](docs/filelock-compatibility.md).
