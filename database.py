import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(os.environ['DATABASE_URL'], convert_unicode=True, encoding="utf8")
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from common.models import Test
    from common.models import Role
    from common.models import User
    Base.metadata.create_all(bind=engine)
    body = {"main-questions": {}, "next": {}}
    init_test = Test("First title", body)
    db_session.add(init_test)
    db_session.commit()
