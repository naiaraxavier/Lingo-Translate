import pytest
from src.models.user_model import UserModel
from src.models.history_model import HistoryModel
import json
from bson import ObjectId


@pytest.fixture
def valid_user():
    user_data = {
        "_id": ObjectId("65738f2224c6e36e4ae23ae1"),
        "name": "token",
        "level": "token",
        "token": "token",
    }
    user = UserModel(user_data)
    user.save()
    return user


def invalid_user():
    user_data = {
        "_id": ObjectId("token"),
        "name": "token",
        "level": "token",
        "token": "token",
    }
    user = UserModel(user_data)
    user.save()
    return user


def test_history_delete(app_test, valid_user):
    HistoryModel(
        {
            "_id": ObjectId("6577888e26d885c273b3c56f"),
            "text_to_translate": "Do you love music?",
            "translate_from": "en",
            "translate_to": "pt",
        }
    ).save()

    history_before_delete = HistoryModel.list_as_json()
    assert len(json.loads(history_before_delete)) == 1

    response = app_test.delete(
        "/admin/history/6577888e26d885c273b3c56f",
        headers={
            "Authorization": valid_user.data["token"],
            "User": valid_user.data["name"],
        },
    )

    assert response.status_code == 204

    history_after_delete = HistoryModel.list_as_json()
    assert len(json.loads(history_after_delete)) == 0

    response = app_test.delete(
        "/admin/history/6577888e26d885c273b3c56f",
        headers={
            "Authorization": "test",
            "User": "test",
        },
    )

    assert response.status_code == 401

    response = app_test.delete(
        "/admin/history/6577888e26d885c273b3c56fdsgdçlhjsdçh",
        headers={
            "Authorization": valid_user.data["token"],
            "User": valid_user.data["name"],
        },
    )

    assert response.status_code == 500

    response = app_test.delete(
        "/admin/history/",
        headers={
            "Authorization": valid_user.data["token"],
            "User": valid_user.data["name"],
        },
    )

    assert response.status_code == 404

    response = app_test.delete(
        "/admin/history/6577888e26d885c273b3c56f",
        headers={
            "Authorization": "",
            "User": valid_user.data["name"],
        },
    )

    assert response.status_code == 401

    response = app_test.delete(
        "/admin/history/6577888e26d885c273b3c56f",
        headers={
            "Authorization": valid_user.data["token"],
            "User": "",
        },
    )

    assert response.status_code == 401

    response = app_test.delete(
        "/admin/history/6577888e26d885c273b3c56f",
        headers={
            "Authorization": invalid_user,
            "User": invalid_user,
        },
    )

    assert response.status_code == 401
