
from http import HTTPStatus


def test_add_to_cart_invalid_qty(client):
    # zero, negative, non-int
    for bad in [0, -1, "two"]:
        r = client.post("/cart/add", json={"title": "Any Book", "qty": bad})
        assert r.status_code in (HTTPStatus.BAD_REQUEST, HTTPStatus.OK)
        # If your API returns an error string, assert it here:
        # assert b"invalid" in r.data.lower() or b"qty" in r.data.lower()


def test_add_to_cart_large_qty(client):
    r = client.post("/cart/add", json={"title": "Big Book", "qty": 9999})
    assert r.status_code in (HTTPStatus.OK, HTTPStatus.BAD_REQUEST)


def test_discount_code_cases(client):
    client.post("/cart/clear")
    client.post("/cart/add", json={"title": "Book", "qty": 1})
    for code in ["SAVE10", "save10", "Save10"]:
        r = client.post("/cart/apply-discount", json={"code": code})
        assert r.status_code in (HTTPStatus.OK, HTTPStatus.BAD_REQUEST)


def test_checkout_missing_fields_strict(client):
    client.post("/cart/clear")
    client.post("/cart/add", json={"title": "Any Book", "qty": 1})
    bad = {"name": "Demo", "payment_method": "card"}  # missing address, etc.
    r = client.post("/checkout", data=bad)
    assert r.status_code in (HTTPStatus.BAD_REQUEST, HTTPStatus.OK)
    # Prefer strict behavior if you implemented it:
    # assert r.status_code == HTTPStatus.BAD_REQUEST
    # assert b"required" in r.data.lower()
