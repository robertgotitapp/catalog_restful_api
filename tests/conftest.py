import pytest
import os
import tempfile
from app import create_app


@pytest.fixture
def app():
    """ Create and configure a new app instance for each test """
    app = create_app()
    yield app


@pytest.fixture
def client(app):
    """ Test client for the application """
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        from app.db import db
        db.init_app(app)

    yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])








