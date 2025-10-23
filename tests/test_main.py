import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_listar_alunos_sucesso():
    response = client.get("/alunos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_buscar_aluno_por_id_sucesso():
    response = client.get("/alunos/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_buscar_aluno_por_id_falha():
    response = client.get("/alunos/999")
    assert response.status_code == 404


def test_criar_aluno_sucesso():
    novo = {"nome": "João Silva", "email": "joao@email.com"}
    response = client.post("/alunos", json=novo)
    assert response.status_code == 200
    assert response.json()["nome"] == "João Silva"


def test_criar_aluno_falha():
    response = client.post("/alunos", json={})
    assert response.status_code == 422  # Falha de validação
