import json
from src.models.history_model import HistoryModel


# Req. 8
def test_request_history(prepare_base):
    history = HistoryModel.list_as_json()
    expected_data = [
        {
            "_id": "6577888e26d885c273b3c56e",
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        },
        {
            "_id": "6577888e26d885c273b3c56f",
            "text_to_translate": "Do you love music?",
            "translate_from": "en",
            "translate_to": "pt",
        },
    ]

    expected_json = json.dumps(expected_data)
    assert history == expected_json
