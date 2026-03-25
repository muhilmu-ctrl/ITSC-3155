from fastapi.testclient import TestClient
from sheep_main import app
import sys
import os
# Add the project root (sheep directory) to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

client = TestClient(app)

def test_read_sheep():
    response = client.get("/sheep/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

def test_add_sheep():
    new_sheep = {
        "id": 7,
        "name": "Jon",
        "breed": "Suffolk",
        "sex": "ram"
    }
    response = client.post("/sheep/{id}", json=new_sheep)
    assert response.status_code == 201
    assert response.json() == new_sheep

    #verification of newly added sheep
    new_response = client.get(f"/sheep/{new_sheep['id']}")
    assert new_response.status_code == 200
    assert new_response.json() == new_sheep