import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_battery():
    client = app.test_client()
    response = client.post('/battery', json={
        "battery": 90,
        "temperature": 25
    })
    assert response.status_code == 200

def test_range():
    client = app.test_client()
    response = client.post('/range', json={
        "battery": 50,
        "traffic": "high",
        "weather": "hot"
    })
    assert response.status_code == 200

def test_charging():
    client = app.test_client()
    response = client.get('/charging')
    assert response.status_code == 200