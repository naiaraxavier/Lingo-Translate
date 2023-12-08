from .abstract_model import AbstractModel
from database.db import db


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, json_data):
        super().__init__(json_data)

    @classmethod
    def list_dicts(cls):
        data = cls._collection.find()
        languages = []
        for language in data:
            languages.append(
                {"name": language["name"], "acronym": language["acronym"]}
            )
        return languages

    def to_dict(self):
        return {
            "name": str(self.data["name"]),
            "acronym": self.data["acronym"],
        }
