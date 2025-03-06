from unittest import TestCase
from unittest.mock import Mock

from src.gmcu.application.usecases.find_project_use_case import FindProjectWithVerifiedInssuanceWithNoOwnerUseCase
from src.gmcu.domain.entities import Issuance, Project, ProjectType, Unit, UnitStatus
from src.gmcu.infrastructure.repository import (
  ProjectRepository,
  IssuanceRepository,
  UnitRepository,
  BaseRepository
)


class FindProjectWithVerifiedInssuanceWithNoOwnerUseCaseTest(TestCase):

    def setUp(self):
        BaseRepository.load = Mock()
        self._project_repository = ProjectRepository(file_path="file.json")
        self._issuance_repository = IssuanceRepository(file_path="file.json")
        self._unit_repository = UnitRepository(file_path="file.json")
        self._usecase = FindProjectWithVerifiedInssuanceWithNoOwnerUseCase(
            project_repository=self._project_repository,
            issuance_repository=self._issuance_repository,
            unit_repository=self._unit_repository
        )

    def test_execute_should_return_expected_result(self):
        self._project_repository._entries = [
            Project(id=1, name="Test Project 1", type=ProjectType.REFORESTATION.value, description="..."),
            Project(id=2, name="Test Project 2", type=ProjectType.DIRECT_REMOVAL.value, description="..."),
        ]
        self._issuance_repository._entries = [
            Issuance(id=1, date="2025-02-01", project_id=1, verified=True),
            Issuance(id=2, date="2025-02-11", project_id=2, verified=True),
            Issuance(id=3, date="2024-03-17", project_id=1, verified=False),
        ]
        self._unit_repository._entries = [
            Unit(id=1, issuance_id=1, owner=None, credits=10, status=UnitStatus.ACTIVE.value),
            Unit(id=2, issuance_id=1, owner=None, credits=10, status=UnitStatus.RETIRED.value),
            Unit(id=3, issuance_id=1, owner="Owner", credits=10, status=UnitStatus.ACTIVE.value),
            Unit(id=4, issuance_id=1, owner=None, credits=70, status=UnitStatus.ACTIVE.value),
            Unit(id=5, issuance_id=2, owner=None, credits=64, status=UnitStatus.ACTIVE.value),
        ]
        self.maxDiff = None
        result = self._usecase.execute()

        self.assertEqual(result.__str__(), "reforestation: {'projects': 1, 'units': 2, 'credits': 80}\ndirect_removal: {'projects': 1, 'units': 1, 'credits': 64}\n")
