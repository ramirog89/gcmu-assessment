from enum import Enum
from dataclasses import dataclass


class ProjectType(Enum):
    REFORESTATION = "reforestation"
    DIRECT_REMOVAL = "direct_removal"


@dataclass
class Project:
  id: int
  name: str
  type: ProjectType
  description: str
