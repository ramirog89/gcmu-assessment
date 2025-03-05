from pkg.domain.entities.unit import Unit
from pkg.infrastructure.repository.base import BaseRepository


class UnitRepository(BaseRepository):

    def __init__(self, file_path: str):
        super().__init__(file_path, cls=Unit)
