from typing import TypedDict, Dict


class DataDto(TypedDict):
    projects: int
    units: int
    credits: int


class ResponseDto:
    results: Dict[str, DataDto] = {}

    def append(self, type: str, data: DataDto):
        self.results[type] = data

    def __str__(self):
        output = ""
        for key, value in self.results.items():
            output += f"{key}: {value}\n"
        return output