# SQLAlchemy quickstart

This is a repo where I learn flask-sqlalchemy from the [official docs](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

## Setup

Here I'm setting up a virtual env to install flask-sqlalchemy module

Terminal - **bash** (commands differ for cmd)

1. Set up virtualenv
    ```bash
    $ virtualenv venv
    ```
2. Activate venv
    ```bash
    $ source venv/scripts/activate
    ```
3. Install required modules
    ```bash
    pip install flask flask-sqlalchemy
    ```
    verisons I'm using:
    - Python 3.9.6
    - flask-2.0.2
    - flask-sqlalchemy-2.5.1

## Quick start

### Initializing a database

To create the initial database, just import the db object from an interactive Python shell and run the SQLAlchemy.create_all() method to create the tables and database:

```py
>>> from app import db
>>> db.create_all()
```

### Creating users, inserting and querying

#### create

```py
>>> from yourapplication import User
>>> admin = User(username='admin', email='admin@example.com')
>>> guest = User(username='guest', email='guest@example.com')
```

#### Insert

```py
>>> db.session.add(admin)
>>> db.session.add(guest)
>>> db.session.commit()
```

#### Query

```py
>>> User.query.all()
[<User u'admin'>, <User u'guest'>]
>>> User.query.filter_by(username='admin').first()
<User u'admin'>
```