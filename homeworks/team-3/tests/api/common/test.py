from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import JSONB
from database import Base


class Test(Base):
    __tablename__ = 'tests'

    id = Column(Integer, primary_key=True)
    body = Column(JSONB)
    title = Column(String)

    def __init__(self, body):
        self.body = body

        def __repr__(self):
            return '<Test %r>' % self.body
