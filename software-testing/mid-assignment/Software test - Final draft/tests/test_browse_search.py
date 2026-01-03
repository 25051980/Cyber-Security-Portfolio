import urllib.parse as url

# TC001-01 Browse by category
def test_browse_by_category(client):
    resp = client.get("/books?category=Fiction")
    assert resp.status_code == 200
    assert b"Fiction" in resp.data

# TC001-02 Unknown category
def test_browse_unknown_category(client):
    resp = client.get("/books?category=Unknown")
    assert resp.status_code in (200, 404)
    if resp.status_code == 200:
        assert b"no results" in resp.data.lower()

# TC001-03 Keyword search
def test_search_keyword(client):
    q = url.quote("Python")
    resp = client.get(f"/search?q={q}")
    assert resp.status_code == 200
    assert b"python" in resp.data.lower() or b"no results" in resp.data.lower()

# TC001-04 Case insensitive + trims
def test_search_case_insensitive(client):
    r1 = client.get("/search?q=Python")
    r2 = client.get("/search?q=%20pYtHon%20")
    assert r1.status_code == 200 and r2.status_code == 200
    assert (r1.data == r2.data) or (
        b"python" in r1.data.lower() and b"python" in r2.data.lower()
    )

# TC001-05 Empty search
def test_search_empty_query(client):
    resp = client.get("/search?q=")
    assert resp.status_code in (200, 400)
    if resp.status_code == 200:
        assert b"enter" in resp.data.lower() or b"search" in resp.data.lower()
