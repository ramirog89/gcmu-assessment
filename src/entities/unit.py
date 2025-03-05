from enum import Enum
from typing import TypedDict, Optional


class UnitStatus(Enum):
    ACTIVE = "active"
    RETIRED = "retired"


class Unit(TypedDict):
  id: int
  issuance_id: int
  owner: Optional[str] = None
  credits: int
  status: UnitStatus
