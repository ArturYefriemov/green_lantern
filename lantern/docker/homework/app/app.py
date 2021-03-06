from flask import Flask
from sqlalchemy_utils import create_database, drop_database, database_exists

from .config import Config
from .populate_data import get_users, get_stores, get_goods
from .models import db, User, Good, Store


def get_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        if database_exists(db.engine.url):
            db.create_all()
            print('Database exists')
        else:
            print(f"Database does not exists {db.engine.url}")
            create_database(db.engine.url)
            print('Data base created')

    with app.app_context():
        users = get_users()
        for user in users:
            db.session.add(User(**user))
        db.session.commit()
        print('Data USERS written in data_base succesfully')

    with app.app_context():
        stores = get_stores()
        for store in stores:
            db.session.add(Store(**store))
        db.session.commit()
        print('Data STORES written in data_base succesfully')

    with app.app_context():
        goods = get_goods()
        for good in goods:
            db.session.add(Good(**good))
        db.session.commit()
        print('Data GOODS written in data_base succesfully')

    return app

