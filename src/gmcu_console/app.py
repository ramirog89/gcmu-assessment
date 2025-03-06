import os
import logging

from src.gmcu.infrastructure.logs.logger import setupLogger
from src.gmcu.infrastructure.repository import ProjectRepository, IssuanceRepository, UnitRepository
from src.gmcu.application.usecases.find_project_use_case import FindProjectWithVerifiedInssuanceWithNoOwnerUseCase
from src.gmcu_console.settings import config

logger = logging.getLogger(__name__)

setupLogger()


class ConsoleApp:

    def __init__(self):
        try:
            self.load_deps()
        except Exception as err:
            logger.error(err)
            exit()

    def load_deps(self):
        project_repository = ProjectRepository(file_path=config['PROJECTS_FILE_PATH'])
        issuance_repository = IssuanceRepository(file_path=config['ISSUANCES_FILE_PATH'])
        unit_repository = UnitRepository(file_path=config['UNITS_FILE_PATH'])

        self._use_case = FindProjectWithVerifiedInssuanceWithNoOwnerUseCase(
          project_repository=project_repository,
          issuance_repository=issuance_repository,
          unit_repository=unit_repository
        )
    
    def run(self):
        response = self._use_case.execute()
        print(response)
