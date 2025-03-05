from enum import Enum
from typing import TypedDict


class ProjectType(Enum):
    REFORESTATION = "reforestation"
    DIRECT_REMOVAL = "direct_removal"


class Project(TypedDict):
  id: id
  name: str
  type: ProjectType
  description: str
