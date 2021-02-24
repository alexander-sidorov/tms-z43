import io

import pytest

from main.sessions import MultipleFilesStorage


class PathMock:
    def __init__(self):
        self.__iodevice = io.StringIO()

    def open(self, mode):
        return self

    def __enter__(self):
        self.__iodevice.seek(0)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def is_file(self) -> bool:
        return True

    def readline(self, *args, **kw):
        return self.__iodevice.readline(*args, **kw)

    def write(self, *args, **kw):
        return self.__iodevice.write(*args, **kw)


@pytest.mark.unit
def test_multiple_file_storage(monkeypatch):
    pm = PathMock()
    monkeypatch.setattr(
        MultipleFilesStorage,
        MultipleFilesStorage._get_storage_file.__name__,
        lambda _a1: pm,
    )

    storage = MultipleFilesStorage("xxx")

    data = storage.load()
    assert data == {"value": []}

    storage.store({"value": [1, 2, 3], "xxx": "yyy"})

    data = storage.load()
    assert data == {"value": [1, 2, 3]}
