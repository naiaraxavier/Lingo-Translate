from flask import Blueprint, jsonify
from models.history_model import HistoryModel
import json

history_controller = Blueprint("history_controller", __name__)


@history_controller.get("/")
def history():
    data = HistoryModel.list_as_json()
    parsed_data = json.loads(data)
    return jsonify(parsed_data), 200
