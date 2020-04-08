from flask import Flask, jsonify, request

import inject


class NoSuchUserError(Exception):
    def __init__(self, user_id):
        self.message = f'No such user_id {user_id}'


app = Flask(__name__)


@app.errorhandler(NoSuchUserError)
def my_error_handler(e):
    return jsonify({'error': e.message}), 404


@app.route('/users', methods=['POST'])
def create_user():
    db = inject.instance('DB')
    user_id = db.users.add(request.json)
    return jsonify({'user_id': user_id}), 201


@app.route('/users/<int:user_id>')
def get_user(user_id):
    db = inject.instance('DB')
    user = db.users.get_user_by_id(user_id)
    return jsonify(user)


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    db = inject.instance('DB')
    db.users.update_user_by_id(user_id, request.json)
    return jsonify({'status': 'success'})


@app.route('/goods', methods=['POST'])
def create_goods():
    db = inject.instance('DB')
    goods_id = db.goods.add(request.json)
    return jsonify({'goods_id': goods_id}), 201


@app.route('/goods/<int:goods_id>')
def get_goods(goods_id):
    db = inject.instance('DB')
    goods = db.goods.get_goods_by_id(goods_id)
    return jsonify(goods)


@app.route('/goods/<int:goods_id>', methods=['PUT'])
def update_goods(goods_id):
    db = inject.instance('DB')
    db.goods.update_goods_by_id(goods_id, request.json)
    return jsonify({'successfully_updated': 1})
