import os

from pkg.infrastructure.repository import ProjectRepository, IssuanceRepository, UnitRepository
from pkg.application.usecases.find_project_use_case import FindProjectUseCase


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECTS_FILE_PATH = f"{BASE_DIR}/projects.json"
ISSUANCES_FILE_PATH = f"{BASE_DIR}/issuances.json"
UNITS_FILE_PATH = f"{BASE_DIR}/units.json"

project_repository = ProjectRepository(file_path=PROJECTS_FILE_PATH)
issuance_repository = IssuanceRepository(file_path=ISSUANCES_FILE_PATH)
unit_repository = UnitRepository(file_path=UNITS_FILE_PATH)

project_use_case = FindProjectUseCase(
  project_repository=project_repository,
  issuance_repository=issuance_repository,
  unit_repository=unit_repository
)

project_use_case.execute()
