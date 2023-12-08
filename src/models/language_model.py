from .abstract_model import AbstractModel
from database.db import db


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, json_data):
        super().__init__(json_data)

    def to_dict(self):
        return {
            "name": str(self.data["name"]),
            "acronym": self.data["acronym"],
        }
