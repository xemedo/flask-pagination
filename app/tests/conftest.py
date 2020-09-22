import pytest
from app import create_app, db


@pytest.fixture
def app():
    app = create_app()
    with app.app_context():
        db.create_all()
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def articles(client):
    def create(count):
        return client.post(
            "/articles",
            json=[
                {"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit"}
            ]
            * count,
        )

    return create
