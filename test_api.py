from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_analyze_route():
    response = client.get("/analyze")

    assert response.status_code == 200

    expected_body = {"status": "success", "message": "Logs analyzed and database updated."}
    assert response.json() == expected_body

def test_blocklist_route():
    response = client.get("/generate-blocklist")

    assert response.status_code == 200

    expected_body = {"status": "success", "message": "Firewall blocklist update."}
    assert response.json() == expected_body

def test_viewer_route():
    response = client.get("/viewer")

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["status"] == "success"
    assert type (response_data["message"]) == list
    