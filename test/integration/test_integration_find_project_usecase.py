import os
from unittest import TestCase

from src.gmcu.application.usecases.find_project_use_case import FindProjectWithVerifiedInssuanceWithNoOwnerUseCase
from src.gmcu.infrastructure.repository import ProjectRepository, IssuanceRepository, UnitRepository


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class TestFindProjectIntegrationTest(TestCase):

    def test_usecase_success(self):
        self._project_repository = ProjectRepository(file_path=f"{BASE_DIR}/fixtures/projects.json")
        self._issuance_repository = IssuanceRepository(file_path=f"{BASE_DIR}/fixtures/issuances.json")
        self._unit_repository = UnitRepository(file_path=f"{BASE_DIR}/fixtures/units.json")
        self._usecase = FindProjectWithVerifiedInssuanceWithNoOwnerUseCase(
            project_repository=self._project_repository,
            issuance_repository=self._issuance_repository,
            unit_repository=self._unit_repository
        )

        response = self._usecase.execute()

        self.assertEqual(response.__str__(), "reforestation: {'projects': 1, 'units': 2, 'credits': 73}\ndirect removal: {'projects': 1, 'units': 6, 'credits': 383}\n")
