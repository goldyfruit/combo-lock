# Combo Lock

The combo-lock is a combination of a process lock and a thread lock. Usable in cases both multiple threads and multiple processes are sharing the same resource such as a file in the file system.

The module utilizes the FileLock from [filelock](https://pypi.org/project/filelock/) and the standard *Lock* from threading.

The FileLock uses a filesystem lock so the initialization of the class requires a path for the lock file.

## Thalovant Compatibility Fork

This fork builds on upstream 0.3.1 and keeps the classic `FileLock` implementation
unchanged. On Python 3.11 and newer, its package metadata requires
`filelock>=4.2.1,<5`, which includes the fix for CVE-2026-112940. The compatibility
tests cover context reuse, non-blocking contention between threads and processes,
and named locks. No `ReadWriteLock` or `SoftReadWriteLock` API is used.

Python 3.10 uses the exact compatibility pin `filelock==3.20.3`, rather than an
unbounded 3.x range. That version contains the earlier TOCTOU fixes and predates
the reader/writer-lock feature affected by CVE-2026-112940. It is outside the
affected ranges of all eight filelock advisories published in the GitHub Advisory
Database when checked on 2026-10-25. It is a compatibility pin, not a backport of
filelock 4 or a guarantee against future findings. See [the recorded advisory
ranges](docs/filelock-compatibility.md).

This Thalovant compatibility fork requires Python 3.10 or newer. It does not
retain upstream's older Python classifiers or claim that Python 3.5-3.9 can use
these dependencies. Consumers must regenerate their dependency locks. This fork
is consumed by immutable Git commit; it is not a PyPI release.

## Example

```python
from combo_lock import ComboLock

lock = ComboLock('/tmp/my.lock')

with lock:
    write_my_shared_resource()


```

A `NamedLock` will save the lock file to shared memory using [memory-tempfile](https://github.com/mbello/memory-tempfile)

```python
from combo_lock import NamedLock

lock = NamedLock('some_name')

with lock:
    write_my_shared_resource()
```

### History

The combo-lock was originally created for [Mycroft-core](https://github.com/mycroftai/mycroft-core) but as it's been useful in other projects a separate release seemed appropriate.
