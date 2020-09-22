import json
from app import db
from app.models.article import Article


def test_create_article(app, client, articles):
    with app.app_context():
        response = articles(1)
        assert response.status_code == 200
        assert db.session.query(Article).count() == 1


def test_create_multiple_articles(app, client, articles):
    with app.app_context():
        response = articles(4)
        assert response.status_code == 200
        assert db.session.query(Article).count() == 4


def test_get_results_sql_alchemy(app, client, articles):
    articles(40)
    resp = client.get("/articles_alchemy?page=1")
    assert len(json.loads(resp.data)) == 5


def test_get_results_flask_paginate(app, client, articles):
    articles(40)
    resp = client.get("/articles_flask_paginate?page=1")
    assert len(json.loads(resp.data)["data"]) == app.config["PAGINATE_PAGE_SIZE"]


def test_get_results_flask_resty(app, client, articles):
    articles(40)
    resp = client.get("/articles_flask_resty?page=0")
    assert len(json.loads(resp.data)["data"]) == 5
