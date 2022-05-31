from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_1_new_calc():
    response = client.post(
        "/v2/newcalc",
        headers={"Content-Type": "application/json"},
        json={
            "waist": 79,
            "hips": 108,
            "type": 0,
            "measure_type": "cm"
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        True
    }


def test_2_new_calc():
    response = client.post(
        "/v2/newcalc",
        headers={"Content-Type": "application/json"},
        json={
            "waist": 71,
            "hips": 112,
            "type": 0,
            "measure_type": "cm"
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        True
    }


def test_3_new_calc():
    response = client.post(
        "/v2/newcalc",
        headers={"Content-Type": "application/json"},
        json={
            "waist": 30.7,
            "hips": 40.9,
            "type": 0,
            "measure_type": "in"
        },
    )


###############################BAD REQUEST########################3


def test_3_new_calc_failed():
    response = client.post(
        "/v2/newcalc",
        headers={"Content-Type": "application/json"},
        json={
            "waist": 79,
            "hips": 100,
            "type": 1,
            "measure_type": "cm"
        },
    )
    assert response.status_code == 400
    assert response.json() == {
        "error_code": 400,
        "error_message": "Model Calculator Bad Request",
        "error_detail": None
    }
