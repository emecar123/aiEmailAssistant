import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from app import create_app, db

@pytest.fixture()
def app_instance(tmp_path):
    app = create_app()
    app.config["TESTING"] = True
    db_path = tmp_path / "test.db"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    with app.app_context():
        db.drop_all()
        db.create_all()
        yield app

@pytest.fixture()
def client(app_instance):
    return app_instance.test_client()
