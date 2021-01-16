from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200


def test_get_place_reservations():
    response = client.get("/place-reservations/")
    assert response.status_code == 200


def test_get_place_reservation():
    response = client.get("/place-reservations/PR0")
    assert response.status_code == 200


def test_patch_place_reservation():
    response = client.patch("/place-reservations/PR0")
    assert response.status_code == 200


def test_post_place_reservation():
    response = client.post(
        "/place-reservations/",
        json={"name": "foobar", "phone": "Foo Bar", "date": "2020-02-03"},
    )
    assert response.status_code == 200


def test_delete_place_reservation():
    response = client.delete("/place-reservations/PR0")
    assert response.status_code == 200
