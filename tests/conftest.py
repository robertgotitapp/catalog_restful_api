import pytest
from app import create_app
from cfg import test


@pytest.fixture
def app():
    from app.db import init_db, clear_db, create_mock_data

    app = create_app()
    app.config.from_object(test)

    with app.app_context():
        init_db()
        create_mock_data()

    yield app
    clear_db()


@pytest.fixture
def client(app):
    return app.test_client()
