import pytest
import os
from app import create_app, db
from cfg import test

# @pytest.fixture
# def app():
#     """ Create and configure a new app instance for each test """
#     app = create_app()
#     app.config.from_object(test)
#     return app


# @pytest.fixture
# def db(app, request):
#
#
#     def teardown():
#         db.clear_db()
#
#     db.clear_db()
#     db.init_app()
#     db.init_db()
#
#     request.addfinalizer(teardown)
#     return db



# @pytest.fixture
# def client(app):
#     """ Test client for the application """
#     app.config['TESTING'] = True
#     client = app.test_client()
#
#     with app.app_context():
#         from app.db import init_db
#         init_db()
#
#     yield client
#
#     os.unlink(app.config['DATABASE'])

@pytest.fixture
def app():
    from app.db import init_db, clear_db

    app = create_app()
    app.config.from_object(test)

    with app.app_context():
        # Create db
        init_db()

    yield app

    # Remove db
    clear_db()


@pytest.fixture
def client(app):
    return app.test_client()








