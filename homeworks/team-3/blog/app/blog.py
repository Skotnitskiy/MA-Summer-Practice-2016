import os
from flask import Flask, request, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template

blog = Flask(__name__)
blog.config.from_object(os.environ['APP_SETTINGS'])
blog.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(blog)

@blog.route('/view', methods=['GET'])
def view():
    from post import Post
    posts = Post.query.all()
    return render_template('index.html', posts=posts)