import importlib, pytest
app_module = importlib.import_module("app")
flask_app = app_module.app
flask_app.config.update(TESTING=True, WTF_CSRF_ENABLED=False, SECRET_KEY="test-secret-key")

@pytest.fixture(scope="session")
def app():
    return flask_app

@pytest.fixture()
def client(app):
    with app.test_client() as c:
        yield c
