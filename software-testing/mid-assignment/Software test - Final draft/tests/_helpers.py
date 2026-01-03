from typing import Iterable, Optional
from bs4 import BeautifulSoup
import time, pytest

def soup(response) -> BeautifulSoup:
    return BeautifulSoup(response.get_data(as_text=True), "html.parser")

def route_set(client) -> set:
    return {r.rule for r in client.application.url_map.iter_rules()}

def pick(routes: Iterable[str], *candidates: str, required: bool=False, default: Optional[str]=None) -> Optional[str]:
    rset = set(routes)
    for c in candidates:
        if c in rset:
            return c
    if required:
        pytest.skip(f"Missing required route (tried {candidates})")
    return default

def ok(resp, code=200):
    assert resp.status_code == code, f"Expected {code}, got {resp.status_code}"

def has_text(html_or_resp, text):
    body = html_or_resp if isinstance(html_or_resp, str) else html_or_resp.get_data(as_text=True)
    assert text in body, f"Expected to find text: {text!r}"

def post_form(client, url: str, data: dict):
    return client.post(url, data=data, follow_redirects=True)

class Stopwatch:
    def __enter__(self): self.t0=time.perf_counter(); return self
    def __exit__(self, *exc): self.elapsed=time.perf_counter()-self.t0
