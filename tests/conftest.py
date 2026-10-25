"""Keep the upstream named-lock tests out of shared machine lock directories."""

from pathlib import Path

import pytest


@pytest.fixture(autouse=True)
def isolated_memory_directory(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Keep every test's named lock files inside its disposable directory."""
    monkeypatch.setattr("combo_lock.util.MemoryTempfile.gettempdir", lambda _: str(tmp_path))
