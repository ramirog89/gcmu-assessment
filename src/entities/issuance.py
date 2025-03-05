from typing import TypedDict


class Issuance(TypedDict):
  id: int
  date: str
  project_id: int
  verified: bool
