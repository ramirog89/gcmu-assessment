from typing import List

from src.gmcu.domain.entities.issuance import Issuance
from src.gmcu.infrastructure.repository.base import BaseRepository


class IssuanceRepository(BaseRepository):

    _entries: List[Issuance]

    def __init__(self, file_path: str):
        super().__init__(file_path, cls=Issuance)

    def find_verified_by_ids(self, ids: List[int]) -> List[Issuance]:
        result = []
        for entry in self._entries:
            if entry.id in ids and entry.verified:
                result.append(entry)
        return result
