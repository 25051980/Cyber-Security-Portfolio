"""
Profile the /checkout flow end-to-end to find hotspots.
Run:  python tools/profile_checkout.py
"""

import cProfile
import pstats
from io import StringIO

from app import app  # expects app.py at repo root


def run_flow():
    with app.test_client() as client:
        # simple cart fill
        client.post("/cart/add", data={"book_id": "B001", "quantity": 2})
        # checkout form (happy path)
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
        client.post("/checkout", data=form, follow_redirects=True)


if __name__ == "__main__":
    pr = cProfile.Profile()
    pr.enable()
    run_flow()
    pr.disable()
    s = StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats(pstats.SortKey.CUMULATIVE)
    ps.print_stats(40)
    print(s.getvalue())
