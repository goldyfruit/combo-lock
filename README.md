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

Python versions below 3.11 retain the upstream `filelock~=3.0` dependency because
filelock 4 requires Python 3.11. **That legacy branch is not security-remediated**:
it may resolve an advisory-affected filelock release. Applications requiring the
fixed dependency must run Python 3.11 or newer and regenerate their dependency
locks. This fork is consumed by immutable Git commit; it is not a PyPI release.

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
