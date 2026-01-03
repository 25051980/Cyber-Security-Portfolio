# 🧪 Testing & CI/CD Summary – Online Bookstore Flask

This project demonstrates a complete automated testing and CI/CD setup for a Flask web application.  
It was developed for academic purposes and implements continuous integration, code quality checks, and performance profiling.

---

## ✅ Overview
- **Repository:** [Online Bookstore Flask](https://github.com/25051980/online_bookstore_flask)
- **Language:** Python 3.9  
- **Framework:** Flask  
- **CI/CD:** GitHub Actions  
- **Testing Tools:** Pytest, Flake8, Bandit, Coverage.py  

---

## 🧠 Features Tested
| Feature | Description |
|----------|--------------|
| 🏠 Home | Homepage renders correctly |
| 🛒 Cart | Add, view, and clear cart items |
| �� Discounts | Apply discount codes via multiple endpoints |
| 💳 Checkout | Validate required fields and confirm order |
| ⚙️ App Factory | Supports test configuration setup |

---

## 🚀 Continuous Integration Workflow
Every commit triggers the workflow **`.github/workflows/ci.yml`**:
1. Install dependencies  
2. Run linting (`flake8`)  
3. Run security scans (`bandit`)  
4. Run tests with coverage (`pytest --cov`)  
5. Upload coverage report artifact

✅ **All tests passing (100% coverage)**  
✅ **No lint or security errors detected**

---

## ⚡ Performance & Profiling
- Benchmarked with `tools/benchmark_pricing.py`
- Profiled with `tools/profile_checkout.py`



✔ Checkout flow is optimized, with no performance bottlenecks.

---

## 📊 Documentation
Full details are available in the [TESTING_REPORT.md](./TESTING_REPORT.md) file, including:
- Coverage results  
- Performance benchmarks  
- CI/CD evidence  
- Next steps for improvement  

---

## 🏁 Summary
This repository shows how to:
- Integrate **automated tests** with **GitHub Actions**
- Maintain **high code quality** and **security compliance**
- Benchmark and profile Flask routes for performance

🎯 Result: A fully validated, maintainable, and production-ready testing pipeline.
