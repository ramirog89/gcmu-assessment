from unittest import TestCase
from unittest.mock import Mock

from src.gmcu.domain.entities import Issuance
from src.gmcu.infrastructure.repository import IssuanceRepository, BaseRepository


class IssuanceRepositoryTest(TestCase):

    def test_find_verified_by_ids_should_return_expected_result(self):
        BaseRepository.load = Mock()
        BaseRepository._entries = [
            Issuance(id=1, date="2025-02-01", project_id=1, verified=True),
            Issuance(id=2, date="2025-02-11", project_id=1, verified=True),
            Issuance(id=3, date="2024-03-17", project_id=2, verified=False),
        ]
        self._base_repo = IssuanceRepository(file_path="file.json")

        result = self._base_repo.find_verified_by_ids(ids=[1, 2, 3])

        self.assertTrue(len(result) == 2)
        self.assertTrue(result[0].id == 1)
        self.assertTrue(result[1].id == 2)

    def test_find_verified_by_ids_should_return_empty(self):
        BaseRepository.load = Mock()
        BaseRepository._entries = [
            Issuance(id=1, date="2025-02-01", project_id=1, verified=True),
            Issuance(id=2, date="2025-02-11", project_id=1, verified=True),
            Issuance(id=3, date="2024-03-17", project_id=2, verified=False),
        ]
        self._base_repo = IssuanceRepository(file_path="file.json")

        result = self._base_repo.find_verified_by_ids(ids=[5])

        self.assertTrue(len(result) == 0)
