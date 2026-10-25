"""The classic FileLock contract must work on both supported dependency branches."""

from concurrent.futures import ThreadPoolExecutor
from importlib.metadata import metadata
import multiprocessing
from pathlib import Path

from packaging.requirements import Requirement
from packaging.specifiers import SpecifierSet
from packaging.version import Version
import pytest

from combo_lock import ComboLock, NamedLock


def _contend(path, result):
    lock = ComboLock(path)
    acquired = lock.acquire(blocking=False)
    result.put(acquired)
    if acquired:
        lock.release()


def test_context_releases_and_reacquires(tmp_path):
    lock = ComboLock(tmp_path / "reuse.lock")
    for _ in range(2):
        with lock:
            assert Path(lock.path).is_file()


def test_nonblocking_thread_contention(tmp_path):
    lock = ComboLock(tmp_path / "thread.lock")
    with lock, ThreadPoolExecutor(max_workers=1) as pool:
        assert pool.submit(lock.acquire, False).result(timeout=2) is False
    assert lock.acquire(False) is True
    lock.release()


def test_nonblocking_independent_instances(tmp_path):
    left = ComboLock(tmp_path / "instances.lock")
    right = ComboLock(tmp_path / "instances.lock")
    with left:
        assert right.acquire(False) is False
    assert right.acquire(False) is True
    right.release()


def test_nonblocking_process_contention(tmp_path):
    context = multiprocessing.get_context("spawn")
    path = str(tmp_path / "process.lock")
    results = context.Queue()
    process = context.Process(target=_contend, args=(path, results))
    try:
        with ComboLock(path):
            process.start()
            process.join(timeout=10)
            assert process.exitcode == 0
            assert results.get(timeout=2) is False
        released = ComboLock(path)
        assert released.acquire(False) is True
        released.release()
    finally:
        if process.is_alive():
            process.terminate()
            process.join(timeout=5)
        results.close()
        results.join_thread()


def test_named_lock_reacquires_and_preserves_requested_permissions(tmp_path, monkeypatch):
    monkeypatch.setattr("combo_lock.combo_lock.get_ram_directory", lambda _: str(tmp_path))
    lock = NamedLock("compatibility/scoped")
    for _ in range(2):
        with lock:
            assert Path(lock.path).parent == tmp_path
            assert Path(lock.path).stat().st_mode & 0o666 == 0o666


@pytest.mark.parametrize("python_version", ["3.10", "3.11", "3.12", "3.13", "3.14"])
def test_installed_metadata_selects_one_explicit_filelock_branch(python_version):
    requirements = [Requirement(value) for value in metadata("combo-lock").get_all("Requires-Dist")]
    selected = [value for value in requirements if value.name == "filelock"
                and value.marker.evaluate({"python_version": python_version})]
    assert len(selected) == 1
    requirement = selected[0]
    if Version(python_version) >= Version("3.11"):
        assert "4.2.1" in requirement.specifier
        assert "4.2.4" in requirement.specifier
        assert "4.2.0" not in requirement.specifier
        assert "3.32.7" not in requirement.specifier
        assert "5.0" not in requirement.specifier
    else:
        assert "3.20.3" in requirement.specifier
        assert "3.20.2" not in requirement.specifier
        assert "3.20.4" not in requirement.specifier
        assert "3.32.7" not in requirement.specifier
        assert "4.2.1" not in requirement.specifier


def test_installed_metadata_requires_supported_python():
    supported = SpecifierSet(metadata("combo-lock")["Requires-Python"])
    assert "3.10" in supported
    assert "3.14" in supported
    assert "3.9" not in supported
