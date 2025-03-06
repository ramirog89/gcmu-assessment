import os

from src.gmcu.infrastructure.repository import ProjectRepository, IssuanceRepository, UnitRepository
from src.gmcu.application.usecases.find_project_use_case import FindProjectWithVerifiedInssuanceWithNoOwnerUseCase

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECTS_FILE_PATH = f"{BASE_DIR}/projects.json"
ISSUANCES_FILE_PATH = f"{BASE_DIR}/issuances.json"
UNITS_FILE_PATH = f"{BASE_DIR}/units.json"


class ConsoleApp:

    def __init__(self):
        try:
            self.load_deps()
        except Exception as err:
            print(err)
            exit()

    def load_deps(self):
        project_repository = ProjectRepository(file_path=PROJECTS_FILE_PATH)
        issuance_repository = IssuanceRepository(file_path=ISSUANCES_FILE_PATH)
        unit_repository = UnitRepository(file_path=UNITS_FILE_PATH)

        self._use_case = FindProjectWithVerifiedInssuanceWithNoOwnerUseCase(
          project_repository=project_repository,
          issuance_repository=issuance_repository,
          unit_repository=unit_repository
        )
    
    def run(self):
        response = self._use_case.execute()
        print(response)
