from flask.ext.security import UserMixin, RoleMixin
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from database import Base
from sqlalchemy.orm import backref, relationship
from sqlalchemy.schema import Table


class Test(Base):
    __tablename__ = 'tests'

    id = Column(Integer, primary_key=True)
    body = Column(JSONB)
    title = Column(String)

    def __init__(self, title, body):
        self.title = title
        self.body = body

        def __repr__(self):
            return '<Test %d %r %r>' % (self.id, self.title, self.body)


roles_users = Table('roles_users', Base.metadata,
                    Column('user_id', Integer(), ForeignKey('users.id')),
                    Column('role_id', Integer(), ForeignKey('roles.id')))


class Role(Base, RoleMixin):
    __tablename__ = 'roles'
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))


class User(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    active = Column(Boolean())
    confirmed_at = Column(DateTime())
    roles = relationship(Role, secondary=roles_users,
                         backref=backref('users', lazy='dynamic'))
