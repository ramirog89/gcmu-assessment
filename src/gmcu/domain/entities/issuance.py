from dataclasses import dataclass


@dataclass
class Issuance:
  id: int
  date: str
  project_id: int
  verified: bool
