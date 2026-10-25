Last Edit: Codex - 2026-10-25 - Motive: Index verified fork compatibility documentation.

# Combo Lock Documentation

[ComboLock and NamedLock](../combo_lock/combo_lock.py) combine thread and
process exclusion through the classic `FileLock.acquire/release` interface.
This fork changes dependency metadata, not those implementations.

- [Filelock compatibility evidence](filelock-compatibility.md): primary advisory
  ranges, supported Python versions, and dependency selection.
- [Quick facts](../QUICK_FACTS.md): package metadata and entry points.
- [Audit](../AUDIT.md): tested behavior and remaining limits.
- [Maintenance report](../MAINTENANCE_REPORT.md): verification and transparency.
- [FAQ](../FAQ.md) and [suggestions](../SUGGESTIONS.md).
