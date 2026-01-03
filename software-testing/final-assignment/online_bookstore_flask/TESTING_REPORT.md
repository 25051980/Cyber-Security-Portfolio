# Testing & CI/CD Report – Online Bookstore Flask

## 1) Overview
- Repository: https://github.com/25051980/online_bookstore_flask
- Commit SHA submitted: `d55faa4`
- Python: 3.9
- CI: GitHub Actions (`.github/workflows/ci.yml`)
- Summary: Unit/integration tests (routes, cart, discounts, checkout), lint (flake8), security scan (bandit), coverage, and performance tools.

## 2) Coverage & Quality Gates
- Command: `pytest --cov=app --cov-report=term-missing`
- Coverage result: **100%**
- Lint: `flake8` → No critical issues
- Security: `bandit -r .` → 0 High-severity issues

## 3) Performance & Profiling
### Benchmark




### Profile
✅ Conclusion: No performance bottlenecks detected. The checkout route executes in ~3 ms.

## 4) CI/CD Evidence
- Latest passing workflow: https://github.com/25051980/online_bookstore_flask/actions
- Steps: Checkout → Install → Lint → Bandit → Pytest → Upload coverage artifact

## 5) Known Issues / Next Steps
- Future improvement: database persistence layer
- Add authentication and user sessions
- Add UI templates
