from itertools import count
from store_app import NoSuchUserError, NoSuchStoreID


class FakeStorage:
    def __init__(self):
        self._goods = FakeGoods()
        self._users = FakeUsers()
        self._store = FakeStore()

    @property
    def users(self):
        return self._users

    @property
    def goods(self):
        return self._goods

    @property
    def store(self):
        return self._store


class FakeUsers:
    def __init__(self):
        self._users = {}
        self._id_counter = count(1)

    def add(self, user):
        user_id = next(self._id_counter)
        self._users[user_id] = user
        return user_id

    def get_user_by_id(self, user_id):
        try:
            return self._users[user_id]
        except KeyError:
            raise NoSuchUserError(user_id)

    def update_user_by_id(self, user_id, user):
        if user_id in self._users:
            self._users[user_id] = user
        else:
            raise NoSuchUserError(user_id)


class FakeGoods:
    def __init__(self):
        self._goods = {}
        self._id_counter = count(1)

    def add(self, goods):
        goods_id = next(self._id_counter)
        self._goods[goods_id] = goods
        return goods_id

    def get_goods_by_id(self, goods_id):
        return self._goods[goods_id]

    def update_goods_by_id(self, goods_id, goods):
        if goods_id in goods:
            self._goods[goods_id].update(goods)


class FakeStore:
    def __init__(self):
        self._store = {}
        self._id_counter = count(1)

    def add(self, store):
        store_id = next(self._id_counter)
        self._store[store_id] = store
        return store_id

    def get_store_by_id(self, store_id):
        try:
            return self._store[store_id]
        except KeyError:
            raise NoSuchStoreID(store_id)

    def update_store_by_id(self, store_id, store):
        if store_id in self._store:
            self._store[store_id] = store
        else:
            raise NoSuchStoreID(store_id)










