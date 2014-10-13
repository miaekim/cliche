import json

from sqlalchemy.sql.expression import func

from cliche.services.wikipedia import crawler as dbpedia
from cliche.services.wikipedia.work import Work


def test_crawler(monkeypatch, fx_session, fx_celery_app):
    class FakeQuery(object):
        def convert(self):
            return {"results":
                    {"bindings": [{"callret-0": {"value": "250280"}}]}
                    }

    monkeypatch.setattr("SPARQLWrapper.SPARQLWrapper.query", FakeQuery)

    relation_num = dbpedia.count_by_relation(
        p=[
            'dbpprop:author',
            'dbpedia-owl:writer',
            'dbpedia-owl:author'
        ]
    )

    class FakeQuery(object):
        offset = 0

        def convert(self):
            with open('tests/select_relation.json') as fp:
                offset = FakeQuery.offset
                fakeResult = (json.load(fp))[offset:offset+100:]
                FakeQuery.offset += 100
                return {"results": {"bindings": fakeResult}}

    monkeypatch.setattr("SPARQLWrapper.SPARQLWrapper.query", FakeQuery)
    dbpedia.crawl_page(1, relation_num)
    num = fx_session.query(Work).count()
    assert fx_session.query(func.max(Work.revision)).scalar() > 0
    assert num == 100
