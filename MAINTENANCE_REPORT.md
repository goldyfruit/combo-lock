Last Edit: Codex - 2026-10-25 - Motive: Record compatibility changes and actual verification.

# Maintenance Report

## 2026-10-25

- Based the existing fork on upstream 0.3.1, retaining its directory-creation
  race fix. The classic lock implementation in `combo_lock/combo_lock.py` is
  unchanged from upstream.
- Added real dependency markers in `requirements.txt`, Python >=3.10 metadata,
  fork version `0.3.1+thalovant.1`, and tests in
  [test_filelock_compatibility.py](tests/test_filelock_compatibility.py).
- Isolated test files and subprocess interpreters in `tests/conftest.py`,
  `tests/test_lock.py` and `tests/process.py`; bounded subprocess waits.
- Verified 23 tests on Python 3.10.22/filelock 3.20.3,
  Python 3.11.15/filelock 4.2.1, and Python 3.14.8/filelock 4.2.4.
  Wheel/sdist builds and blocking Flake8 checks passed. GitHub CI also passed
  Linux Python 3.10-3.14 and macOS Python 3.11 on the compatibility change.
- No production rollout, package publication, or scanner exception performed.

## Transparency Report

- AI model: Codex, GPT-5-based coding agent; no more specific runtime model ID
  was exposed to this task.
- Actions: inspected dependency metadata and primary advisories, edited package
  constraints/tests/documentation, executed compatibility tests and packaging
  checks, and opened the fork PR.
- Oversight: the owner authorized this fork preparation; the coordinating agent
  reviews the immutable commit before consumer adoption. Human merge/release
  approval has not been substituted with a claim of legal or security warranty.
