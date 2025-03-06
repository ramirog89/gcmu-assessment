import os
from unittest import TestCase

from src.gmcu.domain.entities import Project
from src.gmcu.infrastructure.repository import BaseRepository


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class BaseRepositoryTest(TestCase):

    def test_load_file_success(self):
        valid_file_path = "fixtures/projects.json"
        self._base_repo = BaseRepository(file_path=f"{BASE_DIR}/{valid_file_path}", cls=Project)

        self.assertTrue(len(self._base_repo._data) > 0)
        self.assertTrue(len(self._base_repo._entries) > 0)

    def test_file_not_found_exception(self):
        valid_file_path = "fixtures/not_found.json"

        with self.assertRaises(FileNotFoundError) as context:
            self._base_repo = BaseRepository(file_path=f"{BASE_DIR}/{valid_file_path}", cls=Project)
            self.assertTrue(self._base_repo._data == None)
            self.assertTrue(self._base_repo._entries == None)

        self.assertEqual(str(context.exception), f"File {f"{BASE_DIR}/{valid_file_path}"} Not Found")

    def test_file_is_invalid_exception(self):
        valid_file_path = "fixtures/projects_invalid.json"

        with self.assertRaises(Exception) as context:
            self._base_repo = BaseRepository(file_path=f"{BASE_DIR}/{valid_file_path}", cls=Project)
            self.assertTrue(self._base_repo._data == None)
            self.assertTrue(self._base_repo._entries == None)

        self.assertEqual(str(context.exception), f"File {f"{BASE_DIR}/{valid_file_path}"} Is Invalid")
