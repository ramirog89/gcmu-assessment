import json
from typing import Any, TypeVar, Type, List

T = TypeVar('T', bound='dataclass')

class BaseRepository:

    _data = None
    _entries: List[Type[T]] = []

    def __init__(self, file_path: str, cls: Type[T]):
        self.cls = cls
        self._file_path = file_path
        self.load()

    def load(self) -> Any:
        try:
            with open(self._file_path, 'r') as file:
                self._data = json.load(file)
                try:
                    self._entries = [self.cls(**entry) for entry in self._data]
                except Exception:
                    raise Exception(f"File {self._file_path} Is Invalid")
        except FileNotFoundError:
            raise FileNotFoundError(f"File {self._file_path} Not Found")
