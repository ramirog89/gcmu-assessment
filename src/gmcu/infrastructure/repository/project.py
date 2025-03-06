from typing import List

from src.gmcu.domain.entities.project import Project
from src.gmcu.infrastructure.repository.base import BaseRepository


class ProjectRepository(BaseRepository):

    _entries: List[Project]

    def __init__(self, file_path: str):
        super().__init__(file_path, cls=Project)

    def find_by_ids(self, ids: List[int]) -> List[Project]:
        result = []
        for entry in self._entries:
            if entry.id in ids:
                result.append(entry)
        return result