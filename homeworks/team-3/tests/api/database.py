import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(os.environ['DATABASE_URL'], convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from testq import Test
    Base.metadata.create_all(bind=engine)
    body = {"main-questions": {}, "next": {}}
    init_test = Test(body)
    db_session.add(init_test)
    db_session.commit()

