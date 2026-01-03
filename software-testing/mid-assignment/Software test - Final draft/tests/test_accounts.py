
# tests/test_accounts.py
import pytest
from tests._helpers import route_set, pick, ok, soup, post_form, has_text

def _urls(client):
    routes = route_set(client)
    return dict(
        signup = pick(routes, "/signup", "/register"),
        login  = pick(routes, "/login"),
        logout = pick(routes, "/logout"),
        profile= pick(routes, "/account", "/profile"),
        orders = pick(routes, "/account/orders", "/orders/history"),
    )

@pytest.mark.future
def test_signup_login_logout_profile_update_and_history(client):
    U = _urls(client)
    if not (U["signup"] and U["login"] and U["logout"] and U["profile"]):
        pytest.skip("Account routes incomplete")

    # Signup
    r = post_form(client, U["signup"], {"email":"sam@test.com","password":"Secr3t!!"})
    ok(r)
    has_text(r.get_data(as_text=True), "Welcome")

    # Login
    r = post_form(client, U["login"], {"email":"sam@test.com","password":"Secr3t!!"})
    ok(r)

    # Update profile (name)
    r = post_form(client, U["profile"], {"name":"Samuel W."})
    ok(r)
    has_text(r.get_data(as_text=True), "Samuel W.")

    # View order history
    if U["orders"]:
        r = client.get(U["orders"])
        ok(r)
        assert soup(r).select_one("#order-history")  # FR-006 history list

    # Logout
    r = client.get(U["logout"], follow_redirects=True)
    ok(r)
    has_text(r.get_data(as_text=True), "Log in")
