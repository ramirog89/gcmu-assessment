from pkg.infrastructure.repository import ProjectRepository, IssuanceRepository, UnitRepository

class FindProjectWithVerifiedInssuanceWithNoOwnerUseCase:

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
        verified_issuances = self.issuance_repository.get_verified()
        print(f"verified inssuances: {verified_issuances}")

