from pkg.domain.entities.issuance import Issuance
from pkg.infrastructure.repository.base import BaseRepository


class IssuanceRepository(BaseRepository):

    def __init__(self, file_path: str):
        super().__init__(file_path, cls=Issuance)
