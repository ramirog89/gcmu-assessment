from unittest import TestCase
from unittest.mock import Mock

from src.gmcu.domain.entities import Project, ProjectType
from src.gmcu.infrastructure.repository import ProjectRepository, BaseRepository


class ProjectRepositoryTest(TestCase):

    def test_find_by_ids_should_return_expected_result(self):
        BaseRepository.load = Mock()
        BaseRepository._entries = [
            Project(id=1, name="Test", type=ProjectType.REFORESTATION, description="..."),
            Project(id=2, name="Test 2", type=ProjectType.DIRECT_REMOVAL, description="..."),
        ]
        self._base_repo = ProjectRepository(file_path="file.json")

        result = self._base_repo.find_by_ids(ids=[1, 2])

        self.assertTrue(len(result) == 2)
        self.assertTrue(result[0].id == 1)
        self.assertTrue(result[1].id == 2)

    def test_find_by_ids_should_return_empty(self):
        BaseRepository.load = Mock()
        BaseRepository._entries = [
            Project(id=1, name="Test", type=ProjectType.REFORESTATION, description="..."),
            Project(id=2, name="Test 2", type=ProjectType.DIRECT_REMOVAL, description="..."),
        ]
        self._base_repo = ProjectRepository(file_path="file.json")

        result = self._base_repo.find_by_ids(ids=[3, 4])

        self.assertTrue(len(result) == 0)
