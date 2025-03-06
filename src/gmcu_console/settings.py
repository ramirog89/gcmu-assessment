import os
from pathlib import Path

BASE_DIR = Path(os.getcwd())

config = {
    "BASE_DIR": BASE_DIR,
    "PROJECTS_FILE_PATH": f"{BASE_DIR}/projects.json",
    "ISSUANCES_FILE_PATH": f"{BASE_DIR}/issuances.json",
    "UNITS_FILE_PATH": f"{BASE_DIR}/units.json"
}
