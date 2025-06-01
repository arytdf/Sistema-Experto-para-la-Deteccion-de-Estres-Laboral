# tests/test_api.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_endpoint_inferir():
    payload = {"temperatura": 35, "humedad": 70}
    response = client.post("/api/inferir", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "hechos" in data
    assert data["hechos"]["recomendacion"] == "Hace mucho calor, activar aire acondicionado"
