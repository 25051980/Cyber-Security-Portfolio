from http import HTTPStatus


def test_checkout_success(client):
    # start clean and add an item
    client.post("/cart/clear")
    client.post("/cart/add", json={"title": "Clean Architecture", "qty": 1})

    form = {
        "name": "Demo User",
        "email": "demo@bookstore.com",
        "address": "123 Demo St",
        "city": "Demo City",
        "postcode": "D3 0MO",
        "payment_method": "card",
        "card_number": "4242424242424242",
        "card_expiry": "12/34",
        "card_cvv": "123",
    }
    r = client.post("/checkout", data=form, follow_redirects=True)
    assert r.status_code == HTTPStatus.OK
    page = r.get_data(as_text=True)
    assert "Order Confirmation" in page
    assert "Order ID" in page


def test_checkout_missing_required_fields(client):
    client.post("/cart/clear")
    client.post("/cart/add", json={"title": "Any Book", "qty": 1})
    bad = {"name": "Demo User", "payment_method": "card"}
    r = client.post("/checkout", data=bad)
    # we accept 200 with error text OR 400
    assert r.status_code in (HTTPStatus.OK, HTTPStatus.BAD_REQUEST)
    txt = r.get_data(as_text=True).lower()
    assert "required" in txt or "missing" in txt or "error" in txt
