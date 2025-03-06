from typing import List, Tuple

from src.gmcu.application.dtos import ResponseDto, DataDto
from src.gmcu.domain.entities import Project, ProjectType, Issuance, Unit
from src.gmcu.infrastructure.repository import ProjectRepository, IssuanceRepository, UnitRepository


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

        response = ResponseDto()

        for type in ProjectType:
            p_total = self.count_projects_by_type(projects, type.value)
            u_total, c_total = self.count_active_credits_without_owner(projects=projects, issuances=issuances, units=units, type=type.value)
            response.append(type=type.value, data=DataDto(projects=p_total, units=u_total, credits=c_total))

        return response

    def count_projects_by_type(
        self,
        projects: List[Project],
        type: ProjectType
    ) -> int:
        return len([p for p in projects if p.type == type])
    
    def count_active_credits_without_owner(
        self,
        projects: Project,
        issuances: List[Issuance],
        units: List[Unit],
        type: str
    ) -> Tuple[int, int]:
        if self.is_projects_empty(projects):
            return 0, 0

        project = self.get_proyect_by_type(projects, type)
        if not project:
            return 0, 0

        project_issuance_ids = self.get_project_issuance_ids(issuances=issuances, project_id=project.id)
        t_units = 0
        t_credits = 0
        for u in units:
            if u.issuance_id in project_issuance_ids:
                t_units += 1
                t_credits += u.credits

        return t_units, t_credits

    def is_projects_empty(self, projects) -> bool:
        return len(projects) == 0

    def get_proyect_by_type(self, projects, type) -> Project | None:
        try:
            return next(filter(lambda p: p.type == type, projects))
        except:
            return None

    def get_project_issuance_ids(self, issuances: List[Issuance], project_id: int) -> List[int]:
        return [i.id for i in issuances if i.project_id == project_id]
