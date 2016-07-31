from api import app
from flask.ext.login import login_required
from flask.ext.security import SQLAlchemyUserDatastore, Security
from flask import render_template
from common.models import Role, User
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


# @app.before_first_request
# def create_user():
#     user_datastore.create_user(email='admin@i.ua', password='admin')
#     db.session.commit()

@app.route('/')
@login_required
def index():
    return render_template('index.html')