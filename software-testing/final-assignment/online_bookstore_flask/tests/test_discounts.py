from http import HTTPStatus


def test_apply_save10_and_view_cart(client):
    # reset cart
    client.post("/cart/clear")
    # add one item
    client.post("/cart/add", json={"title": "Clean Code", "qty": 1})

    # apply discount (allow form or json)
    r = client.post("/cart/apply-discount", data={"code": "SAVE10"})
    assert r.status_code == HTTPStatus.OK
    assert "Discount applied: SAVE10" in r.get_data(as_text=True)

    # cart page should show the discount
    page = client.get("/cart").get_data(as_text=True)
    assert "10%" in page or "SAVE10" in page
