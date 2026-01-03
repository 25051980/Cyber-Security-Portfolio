
# tests/test_responsive.py
import pytest
from tests._helpers import ok, soup

@pytest.mark.future
def test_has_viewport_meta_and_mobile_nav(client):
    # We check homepage HTML for responsive markers
    r = client.get("/")
    ok(r)
    page = soup(r)
    # Minimal checks that indicate responsive intent (FR-007)
    vp = page.find("meta", attrs={"name":"viewport"})
    assert vp and "width=device-width" in vp.get("content","")
    # mobile menu/icon exists
    assert page.select_one(".mobile-nav") or page.select_one("[data-mobile-nav]")
