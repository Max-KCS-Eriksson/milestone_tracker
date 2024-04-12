import json
from pathlib import Path

from .milestone import Milestone

MILESTONES_DIR = Path(__file__).parent.resolve()
STORAGE_FILE_NAME = "milestones.json"


class Storage:
    def __init__(self):
        self.storage = f"{MILESTONES_DIR}/{STORAGE_FILE_NAME}"
        self.milestones = self._read_storage_file()

    def _read_storage_file(self):
        try:
            with open(self.storage, "r") as json_file:
                milestones = json.load(json_file)
        except FileNotFoundError:
            with open(self.storage, "w") as json_file:
                milestones = {}
                json.dump(milestones, json_file)

        return milestones

    def add_milestone(self, milestone: Milestone):
        if self.has_milestone(milestone.event):
            return False

        self.milestones[milestone.event] = {
            "year": milestone.year,
            "month": milestone.month,
            "day": milestone.day,
        }

        self._store_milestones()
        return True

    def _store_milestones(self):
        with open(self.storage, "w") as json_file:
            json.dump(self.milestones, json_file)

    def has_milestone(self, event):
        return event in self.milestones
