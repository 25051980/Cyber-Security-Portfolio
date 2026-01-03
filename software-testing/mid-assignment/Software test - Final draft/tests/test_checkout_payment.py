
# tests/test_checkout_payment.py
import pytest, re
from tests._helpers import route_set, pick, soup, ok, post_form, Stopwatch, has_text

pytestmark = pytest.mark.usefixtures("client")

def _urls(client):
    routes = route_set(client)
    return {
        "add_to_cart": pick(routes, "/add_to_cart", "/cart/add", required=True),
        "cart":        pick(routes, "/cart", "/basket", required=True),
        "checkout":    pick(routes, "/checkout", "/cart/checkout"),
        "pay":         pick(routes, "/pay", "/payment/submit"),
        "discount":    pick(routes, "/apply_discount", "/cart/discount"),
        "confirm":     pick(routes, "/order/confirm", "/confirm")
    }

@pytest.mark.future
def test_checkout_lines_shipping_discount_totals(client):
    U = _urls(client)
    # Arrange: add two items
    ok(post_form(client, U["add_to_cart"], {"book_id":"1","qty":"2"}))
    ok(post_form(client, U["add_to_cart"], {"book_id":"2","qty":"1"}))
    # Act: open checkout
    resp = client.get(U["checkout"] or pytest.skip("No checkout route"))
    ok(resp)
    page = soup(resp)
    # Assert: line items + total visible (FR-003)
    assert page.select_one("#order-summary")
    has_text(resp.get_data(as_text=True), "Total")
    # Apply discount code and see total change
    if U["discount"]:
        r2 = post_form(client, U["discount"], {"code":"WELCOME10"})
        ok(r2)
        txt = r2.get_data(as_text=True)
        assert re.search(r"Discount|Promo", txt)
        assert re.search(r"Total.*\\$", txt)  # new total displayed

@pytest.mark.future
def test_payment_success_and_redirect_to_confirmation(client, monkeypatch):
    U = _urls(client)
    if not (U["checkout"] and U["pay"] and U["confirm"]):
        pytest.skip("Payment flow not wired")
    # Fake gateway: patch something like 'app.payments.charge'
    try:
        import app, importlib
        mod = importlib.import_module("app")
    except Exception:
        pytest.skip("App module not importable for monkeypatch")

    def fake_charge(card, amount):
        return {"ok": True, "txn_id": "TX123"}
    monkeypatch.setattr(mod, "charge_card", fake_charge, raising=False)

    # Go to checkout then pay
    ok(client.get(U["checkout"]))
    r = post_form(client, U["pay"], {
        "card_number":"4242424242424242", "exp":"12/30", "cvv":"123"
    })
    ok(r)
    assert r.request.path in (U["confirm"], "/order/confirm")

@pytest.mark.future
def test_payment_failure_surfaces_message(client, monkeypatch):
    U = _urls(client)
    if not (U["checkout"] and U["pay"]):
        pytest.skip("Payment endpoint missing")
    # Fake failing gateway
    import importlib
    try:
        mod = importlib.import_module("app")
    except Exception:
        pytest.skip("App module not importable for monkeypatch")
    def fail_charge(card, amount):
        raise ValueError("Card declined")
    monkeypatch.setattr(mod, "charge_card", fail_charge, raising=False)

    ok(client.get(U["checkout"]))
    r = post_form(client, U["pay"], {"card_number":"4000000000000002",
                                     "exp":"12/30","cvv":"123"})
    ok(r)  # page renders with error
    has_text(r.get_data(as_text=True), "declined")  # FR-004 error surfaced
