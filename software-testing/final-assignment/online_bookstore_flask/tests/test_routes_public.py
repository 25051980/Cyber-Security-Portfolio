from http import HTTPStatus


def test_homepage_renders(client):
    resp = client.get("/")
    assert resp.status_code == HTTPStatus.OK
    assert "Welcome to the Online Bookstore!" in resp.get_data(as_text=True)
