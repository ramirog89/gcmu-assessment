from typing import List

from pkg.application.dtos import ResponseDto, DataDto
from pkg.domain.entities import Project, ProjectType
from pkg.infrastructure.repository import (
  ProjectRepository,
  IssuanceRepository,
  UnitRepository
)


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
        project_ids = list(set([i.project_id for i in issuances]))
        projects = self.project_repository.find_by_ids(ids=project_ids)
        print(f"units: {units}")
        print(f"issuances: {issuances}")
        print(f"projects: {projects}")

        response = ResponseDto()
        for type in ProjectType:
            response.append(
                type=type.value,
                data=DataDto(
                    projects=self.count_projects_by_type(projects, type.value),
                    units=self.count_active_credits_without_owner(projects, type.value, units),
                    credits=0
                )
            )

        return response

    def count_projects_by_type(
        self,
        projects: List[Project],
        type: ProjectType
    ) -> int:
        return len([p for p in projects if p.type == type])
    
    def count_active_credits_without_owner(
        self,
        projects,
        type,
        units
    ) -> int:
        return 0
