from pkg.application.dtos import ResponseDto, DataDto
from pkg.domain.entities import ProjectType
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

    def execute(self) -> ResponseDto:
        units = self.unit_repository.find_active_credits_without_owner()
        issuance_ids = list(set([u.issuance_id for u in units]))
        issuances = self.issuance_repository.find_verified_by_ids(ids=issuance_ids)

        response = ResponseDto()
        for type in ProjectType:
            response.append(type=type.value, data=DataDto(projects=0, units=0, credits=0))

        return response
