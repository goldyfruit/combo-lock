"""Keep the upstream named-lock tests out of shared machine lock directories."""

import pytest


@pytest.fixture(autouse=True)
def isolated_memory_directory(tmp_path, monkeypatch):
    monkeypatch.setattr("combo_lock.util.MemoryTempfile.gettempdir", lambda _: str(tmp_path))
