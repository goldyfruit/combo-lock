Last Edit: Codex - 2026-10-25 - Motive: Record verified dependency remediation and residual risks.

# Audit

## Dependency selection

The upstream broad filelock 3.x range can select versions affected by
CVE-2026-112940. Actual requirements now select exact 3.20.3 for Python 3.10
and >=4.2.1,<5 for newer Python. All eight current advisory ranges are recorded
in [the evidence table](docs/filelock-compatibility.md). No exception was added.

## Verified behavior

[Compatibility tests](tests/test_filelock_compatibility.py) passed on the three
dependency/interpreter combinations in [the maintenance report](MAINTENANCE_REPORT.md).
They verify `ComboLock.acquire`, `release`, context reuse, process/thread
exclusion, `NamedLock` mode, and installed package metadata.

## Remaining limits

- This change is not a full audit of the upstream lock implementation or its
  shared-directory design in [combo_lock/util.py](combo_lock/util.py).
- Exact 3.20.3 is a maintained compatibility selection, not a future security
  guarantee. Consumer vulnerability gates must continue to evaluate it.
- Consumers must regenerate and test their own dependency graphs and artifacts;
  passing this library suite does not itself authorize deployment.
