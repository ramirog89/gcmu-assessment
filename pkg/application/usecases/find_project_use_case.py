from pkg.infrastructure.repository import ProjectRepository, IssuanceRepository, UnitRepository

class FindProjectUseCase:

    def __init__(
        self,
        project_repository: ProjectRepository,
        issuance_repository: IssuanceRepository,
        unit_repository: UnitRepository
    ):
        self.project_repository = project_repository
        self.issuance_repository = issuance_repository
        self.unit_repository = unit_repository

    def execute(self):
        print("project data")
        print(self.project_repository._entries)
        print("issuance data")
        print(self.issuance_repository._entries)
        print("unit data")
        print(self.unit_repository._entries)
