from src.models.user_model import UserModel
from src.models.history_model import HistoryModel
from bson import ObjectId
import pytest
import json


@pytest.fixture
def valid_user():
    user_data = {
        "_id": ObjectId("65738f2224c6e36e4ae23ae1"),
        "name": "Peter",
        "level": "admin",
        "token": "Token_123",
    }
    user = UserModel(user_data)
    user.save()
    return user


# Função auxiliar para criar um histórico válido para exclusão
def create_valid_history_for_deletion():
    HistoryModel(
        {
            "_id": ObjectId("6577888e26d885c273b3c56f"),
            "text_to_translate": "Do you love music?",
            "translate_from": "en",
            "translate_to": "pt",
        }
    ).save()


# Função auxiliar para verificar o número inicial de históricos
def assert_initial_history_count():
    history_before_delete = HistoryModel.list_as_json()
    assert len(json.loads(history_before_delete)) == 1


# Função para testar a exclusão de um histórico válido
def assert_valid_history_deletion(app_test, valid_user):
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


# Função para testar exclusões inválidas (por exemplo, sem autorização)
def assert_unauthorized_history_deletion(app_test, valid_user):
    # Tentativa de exclusão sem autorização
    response = app_test.delete(
        "/admin/history/6577888e26d885c273b3c56f",
        headers={
            "Authorization": "test",
            "User": "test",
        },
    )
    assert response.status_code == 401

    # Tentativa de exclusão com nome e token trocados
    response = app_test.delete(
        "/admin/history/6577888e26d885c273b3c56f",
        headers={
            "Authorization": "Peter",
            "User": "Token_123",
        },
    )
    assert response.status_code == 401

    # Tentativa de exclusão com token e nome de usuário iguais
    response = app_test.delete(
        "/admin/history/6577888e26d885c273b3c56f",
        headers={
            "Authorization": "token",
            "User": "token",
        },
    )
    assert response.status_code == 401

    # Tentativa de exclusão com ID inválido
    response = app_test.delete(
        "/admin/history/6577888e26d885c273b3c56fdsgdçlhjsdçh",
        headers={
            "Authorization": valid_user.data["token"],
            "User": valid_user.data["name"],
        },
    )
    assert response.status_code == 500

    # Tentativa de exclusão em um endpoint inválido
    response = app_test.delete(
        "/admin/history/",
        headers={
            "Authorization": valid_user.data["token"],
            "User": valid_user.data["name"],
        },
    )
    assert response.status_code == 404

    # Tentativa de exclusão sem token de autorização
    response = app_test.delete(
        "/admin/history/6577888e26d885c273b3c56f",
        headers={
            "Authorization": "",
            "User": valid_user.data["name"],
        },
    )
    assert response.status_code == 401

    # Tentativa de exclusão sem nome de usuário
    response = app_test.delete(
        "/admin/history/6577888e26d885c273b3c56f",
        headers={
            "Authorization": valid_user.data["token"],
            "User": "",
        },
    )
    assert response.status_code == 401

    # Tentativa de exclusão com usuários inválidos
    response = app_test.delete(
        "/admin/history/6577888e26d885c273b3c56f",
        headers={
            "Authorization": "invalid_user",
            "User": "invalid_user",
        },
    )
    assert response.status_code == 401


def test_history_delete(app_test, valid_user):
    create_valid_history_for_deletion()
    assert_initial_history_count()
    assert_valid_history_deletion(app_test, valid_user)
    assert_unauthorized_history_deletion(app_test, valid_user)
