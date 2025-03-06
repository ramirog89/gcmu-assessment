from unittest import TestCase
from unittest.mock import Mock

from src.gmcu.domain.entities import Unit, UnitStatus
from src.gmcu.infrastructure.repository import UnitRepository, BaseRepository


class UnitRepositoryTest(TestCase):

    def test_find_active_credits_without_owner_should_return_expected_result(self):
        BaseRepository.load = Mock()
        BaseRepository._entries = [
            Unit(id=1, issuance_id=2, owner=None, credits=10, status=UnitStatus.ACTIVE.value),
            Unit(id=2, issuance_id=2, owner="Owner Name", credits=5, status=UnitStatus.ACTIVE.value),
            Unit(id=3, issuance_id=2, owner=None, credits=5, status=UnitStatus.RETIRED.value),
        ]
        self._base_repo = UnitRepository(file_path="file.json")

        result = self._base_repo.find_active_credits_without_owner()

        self.assertTrue(len(result) == 1)
        self.assertTrue(result[0].id == 1)


    def test_find_active_credits_without_owner_should_return_empty(self):
        BaseRepository.load = Mock()
        BaseRepository._entries = [
            Unit(id=1, issuance_id=2, owner=None, credits=10, status=UnitStatus.RETIRED.value),
            Unit(id=2, issuance_id=2, owner="Owner Name", credits=5, status=UnitStatus.ACTIVE.value),
            Unit(id=3, issuance_id=2, owner=None, credits=5, status=UnitStatus.RETIRED.value),
        ]
        self._base_repo = UnitRepository(file_path="file.json")

        result = self._base_repo.find_active_credits_without_owner()

        self.assertTrue(len(result) == 0)
