from http import HTTPStatus


def test_cart_empty(client):
    r = client.get("/cart")
    assert r.status_code == HTTPStatus.OK
    assert "Your cart is empty" in r.get_data(as_text=True)


def test_cart_add_and_view(client):
    # add one item
    r = client.post("/cart/add", data={"title": "Clean Code"})
    assert r.status_code == HTTPStatus.OK
    assert "Added to cart: Clean Code" in r.get_data(as_text=True)

    # view cart should show count 1
    r = client.get("/cart")
    assert r.status_code == HTTPStatus.OK
    assert "Cart items: 1" in r.get_data(as_text=True)
