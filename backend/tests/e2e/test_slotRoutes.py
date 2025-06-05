from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def testGetAvailableSlotsRoutes():
    response = client.get("/slots")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for slot in data:
        assert slot["isAvailable"] == True
