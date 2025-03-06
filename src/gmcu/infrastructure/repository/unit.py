from typing import List

from src.gmcu.domain.entities.unit import Unit
from src.gmcu.infrastructure.repository.base import BaseRepository


class UnitRepository(BaseRepository):

    _entries: List[Unit]

    def __init__(self, file_path: str):
        super().__init__(file_path, cls=Unit)

    def find_active_credits_without_owner(self) -> List[Unit]:
        result = []
        for entry in self._entries:
            if entry.is_active() and not entry.has_owner():
                result.append(entry)
        return result