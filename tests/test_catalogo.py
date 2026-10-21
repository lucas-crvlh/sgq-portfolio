"""Tests run solely against temporary fictional data."""

import pytest
from fastapi.testclient import TestClient

from app.main import create_app


@pytest.fixture
def client(tmp_path):
    application = create_app(f"sqlite:///{tmp_path / 'catalogo_test.db'}")
    with TestClient(application) as test_client:
        yield test_client


@pytest.fixture
def norma_ficticia():
    return {
        "codigo": "DEMO-NORMA-001",
        "titulo": "Documento demonstrativo de medição",
        "revisao": "R1",
        "organismo_emissor": "Organismo Fictício",
    }


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_retrieve(client, norma_ficticia):
    created = client.post("/normas", json=norma_ficticia)
    assert created.status_code == 201
    assert created.json()["id"] >= 1
    fetched = client.get("/normas/DEMO-NORMA-001")
    assert fetched.status_code == 200
    assert {k: v for k, v in fetched.json().items() if k != "id"} == norma_ficticia


def test_normalizes_code_and_trims_fields(client, norma_ficticia):
    norma_ficticia["codigo"] = "  demo-norma-001  "
    norma_ficticia["titulo"] = "  Documento demonstrativo de medição  "
    created = client.post("/normas", json=norma_ficticia)
    assert created.status_code == 201
    assert created.json()["codigo"] == "DEMO-NORMA-001"
    assert created.json()["titulo"] == "Documento demonstrativo de medição"
    assert client.get("/normas/demo-norma-001").status_code == 200


def test_duplicate_code_returns_409(client, norma_ficticia):
    assert client.post("/normas", json=norma_ficticia).status_code == 201
    norma_ficticia["codigo"] = " demo-norma-001 "
    duplicate = client.post("/normas", json=norma_ficticia)
    assert duplicate.status_code == 409
    assert duplicate.json()["detail"] == "Código já cadastrado"
    assert len(client.get("/normas").json()) == 1


@pytest.mark.parametrize("payload", [
    {"codigo": "A", "titulo": "Título de exemplo", "revisao": "R1", "organismo_emissor": "Emissor X"},
    {"codigo": "DEMO-NORMA-001", "titulo": "  ", "revisao": "R1", "organismo_emissor": "Emissor X"},
    {"codigo": "DEMO / 001", "titulo": "Título de exemplo", "revisao": "R1", "organismo_emissor": "Emissor X"},
    {"codigo": "DEMO-NORMA-001", "titulo": "Título de exemplo", "organismo_emissor": "Emissor X"},
])
def test_invalid_input_returns_422_and_does_not_write(client, payload):
    response = client.post("/normas", json=payload)
    assert response.status_code == 422
    assert client.get("/normas").json() == []


def test_get_nonexistent_norma_returns_404(client):
    response = client.get("/normas/DEMO-NAO-EXISTE")
    assert response.status_code == 404


def test_list_order_and_pagination(client, norma_ficticia):
    for codigo in ["DEMO-003", "DEMO-001", "DEMO-002"]:
        assert client.post("/normas", json={**norma_ficticia, "codigo": codigo}).status_code == 201
    response = client.get("/normas?limit=2&offset=1")
    assert response.status_code == 200
    assert [x["codigo"] for x in response.json()] == ["DEMO-002", "DEMO-003"]


def test_invalid_pagination_returns_422(client):
    assert client.get("/normas?limit=0").status_code == 422
    assert client.get("/normas?offset=-1").status_code == 422


def test_persists_between_application_restarts(tmp_path, norma_ficticia):
    url = f"sqlite:///{tmp_path / 'persistent.db'}"
    with TestClient(create_app(url)) as first:
        assert first.post("/normas", json=norma_ficticia).status_code == 201
    with TestClient(create_app(url)) as second:
        assert second.get("/normas/DEMO-NORMA-001").status_code == 200
