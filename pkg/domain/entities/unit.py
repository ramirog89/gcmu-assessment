from enum import Enum
from typing import Optional
from dataclasses import dataclass

class UnitStatus(Enum):
    ACTIVE = "active"
    RETIRED = "retired"


@dataclass
class Unit:
  id: int
  issuance_id: int
  owner: Optional[str]
  credits: int
  status: UnitStatus
