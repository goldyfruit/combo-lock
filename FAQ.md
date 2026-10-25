Last Edit: Codex - 2026-10-25 - Motive: Explain supported Python and filelock compatibility boundaries.

# FAQ

## Why not keep filelock ~=3.0 everywhere?

That broad range can select advisory-affected versions. Python 3.10 uses exact
3.20.3, outside all eight recorded advisory ranges; newer Python uses >=4.2.1,<5.
[The recorded ranges](docs/filelock-compatibility.md) are dated evidence, not a
promise that either branch will remain safe from future findings.

## Does the fork change lock behavior?

No. [ComboLock.acquire/release and NamedLock](combo_lock/combo_lock.py) remain
the upstream 0.3.1 implementation. [Tests](tests/test_filelock_compatibility.py)
exercise the actual classic FileLock API, not reader/writer locks.

## Is this a published PyPI package?

No. Applications can review and pin the immutable fork archive. Published
libraries must not assume that a direct-URL dependency is accepted by PyPI.
