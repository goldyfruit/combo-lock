Last Edit: Codex - 2026-10-25 - Motive: Record focused follow-up work without expanding this patch.

# Suggestions

| Problem | Proposed follow-up | Expected impact |
| --- | --- | --- |
| An application-only fork creates maintenance ownership | Offer the tested classic FileLock compatibility changes upstream after review | Reduce long-term fork upkeep |
| Future advisories may invalidate the Python 3.10 pin | Recheck advisory ranges during consumer release scans and refresh tests | Prevent stale security assumptions |
| Shared named-lock paths are outside this dependency audit | Separately review `NamedLock` and `get_ram_directory` in [combo_lock/combo_lock.py](combo_lock/combo_lock.py) and [combo_lock/util.py](combo_lock/util.py) | Clarify filesystem trust boundaries without changing current behavior |
