from pkg.domain.entities.project import Project
from pkg.infrastructure.repository.base import BaseRepository


class ProjectRepository(BaseRepository):

    def __init__(self, file_path: str):
        super().__init__(file_path, cls=Project)
