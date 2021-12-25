from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

app = Flask(__name__)

file_path = os.path.abspath(os.getcwd())+"/test1.db"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

'''
CREATE TABLE Post (
        id INTEGER NOT NULL,
        title VARCHAR(80) NOT NULL,
        body TEXT NOT NULL,
        pub_date DATETIME NOT NULL,
        category_id INTEGER,
        PRIMARY KEY (id),
        FOREIGN KEY (category_id) REFERENCES Category(id)
);
CREATE TABLE Category (
        id INTEGER NOT NULL,
        name VARCHAR(50) NOT NULL,
        PRIMARY KEY (id)
);
'''


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
                         default=datetime.utcnow)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
                            nullable=False)
    category = db.relationship('Category',
                               backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name


if __name__ == "__main__":
    # py = Category(name='Python')
    # Post(title='Hello Python!', body='Python is pretty cool', category=py)
    # p = Post(title='Snakes', body='Ssssssss')
    # py.posts.append(p)
    # db.session.add(py)
    # db.session.commit()

    posts = Post.query.all()
    print('----posts----')
    for post in posts:
        print('post.id', post.id)
        print('post.title', post.title)
        print('post.body', post.body)
        print('post.pub_date', post.pub_date)
        print('post.category_id', post.category_id)
    
    print('\n-------------\n')
    
    categories = Category.query.all()
    print('----categories----')
    for category in categories:
        print(category)
        print('posts in category', category.posts)
