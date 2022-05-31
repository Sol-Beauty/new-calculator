from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_min_limit_old_cloth_success():
    response = client.post(
        "/v1/predictor",
        headers={"Content-Type": "application/json"},
        json={
            "waist": 68,
            "hips": 103,
            "type": 1,
            "measure_type": "cm"
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "size": "0/8"
    }


def test_max_limit_old_cloth_success():
    response = client.post(
        "/v1/predictor",
        headers={"Content-Type": "application/json"},
        json={
            "waist": 103,
            "hips": 138,
            "type": 1,
            "measure_type": "cm"
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "size": "16/20"
    }


def test_min_limit_new_cloth_success():
    response = client.post(
        "/v1/predictor",
        headers={"Content-Type": "application/json"},
        json={
            "waist": 66,
            "hips": 101,
            "type": 0,
            "measure_type": "cm"
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "size": "0/8"
    }


def test_max_limit_new_cloth_success():
    response = client.post(
        "/v1/predictor",
        headers={"Content-Type": "application/json"},
        json={
            "waist": 101,
            "hips": 138,
            "type": 0,
            "measure_type": "cm"
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "size": "12/18"
    }


################################################################

def test_min_limit_old_cloth_failed():
    response = client.post(
        "/v1/predictor",
        headers={"Content-Type": "application/json"},
        json={
            "waist": 67,
            "hips": 103,
            "type": 1,
            "measure_type": "cm"
        },
    )
    assert response.status_code == 400
    assert response.json() == {
        "error_code": 400,
        "error_message": "Model predictor bad request",
        "error_detail": None
    }


def test_max_limit_old_cloth_failed():
    response = client.post(
        "/v1/predictor",
        headers={"Content-Type": "application/json"},
        json={
            "waist": 103,
            "hips": 140,
            "type": 1,
            "measure_type": "cm"
        },
    )
    assert response.status_code == 400
    assert response.json() == {
        "error_code": 400,
        "error_message": "Model predictor bad request",
        "error_detail": None
    }


def test_min_limit_new_cloth_failed():
    response = client.post(
        "/v1/predictor",
        headers={"Content-Type": "application/json"},
        json={
            "waist": 66,
            "hips": 100,
            "type": 0,
            "measure_type": "cm"
        },
    )
    assert response.status_code == 400
    assert response.json() == {
        "error_code": 400,
        "error_message": "Model predictor bad request",
        "error_detail": None
    }


def test_max_limit_new_cloth_failed():
    response = client.post(
        "/v1/predictor",
        headers={"Content-Type": "application/json"},
        json={
            "waist": 105,
            "hips": 138,
            "type": 0,
            "measure_type": "cm"
        },
    )
    assert response.status_code == 400
    assert response.json() == {
        "error_code": 400,
        "error_message": "Model predictor bad request",
        "error_detail": None
    }
