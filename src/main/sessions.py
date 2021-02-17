import abc
import os
from pathlib import Path
from typing import Dict
from typing import List
from typing import Optional
from typing import Type
from typing import Union

from framework.dirs import DIR_STORAGE

SessionValueT = Union[None, int, float, str, List, Dict]
SessionT = Dict[str, SessionValueT]


class SessionStorage(abc.ABC):
    def __init__(self, session_id: str):
        self._session_id = session_id

    @abc.abstractmethod
    def load(self) -> SessionT:
        raise NotImplementedError

    @abc.abstractmethod
    def store(self, session_data: SessionT) -> None:
        raise NotImplementedError


class MultipleFilesStorage(SessionStorage):
    def load(self) -> SessionT:
        file_path = self._get_storage_file()
        if not file_path.is_file():
            value = []
        else:
            with file_path.open("r") as src:
                line = src.readline()
                value = eval(line) if line else []
        return {"value": value}

    def store(self, session_data: SessionT) -> None:
        if "value" not in session_data:
            raise ValueError('malformed session data: no "value" key')
        value = session_data["value"]
        file_path = self._get_storage_file()
        with file_path.open("w") as dst:
            dst.write(str(value))

    def _get_storage_file(self) -> Path:
        file_path = DIR_STORAGE / f"{self._session_id}.txt"
        return file_path


class Session:
    def __init__(
            self,
            session_id: Optional[str] = None,
            storage_factory: Type[SessionStorage] = MultipleFilesStorage,
    ):
        self.__session_id = session_id or self.generate_session_id()
        self.__storage_factory = storage_factory
        self.__storage: Optional[SessionStorage] = self.__storage_factory(
            self.__session_id
        )

    @staticmethod
    def generate_session_id() -> str:
        return os.urandom(8).hex()

    @property
    def id(self) -> str:
        return self.__session_id

    @property
    def storage(self) -> SessionStorage:
        if not self.__storage:
            self.__storage = self.__storage_factory(self.__session_id)
        return self.__storage

    def __getitem__(self, key: str) -> SessionValueT:
        data = self.storage.load()
        item = data.get(key)
        return item

    def __setitem__(self, key: str, value: SessionValueT) -> None:
        data = self.storage.load()
        data[key] = value
        self.storage.store(data)

    def headers_list(self) -> List:
        return [("Set-Cookie", f"z43sessionid={self.id}")]
