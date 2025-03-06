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

  def is_active(self) -> bool:
    return self.status == UnitStatus.ACTIVE.value

  def has_owner(self) -> bool:
     return self.owner != None
