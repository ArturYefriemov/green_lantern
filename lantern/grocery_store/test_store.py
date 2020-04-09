import inject

from store_app import app
from fake_storage import FakeStorage


def configure_test(binder):
    db = FakeStorage()
    binder.bind('DB', db)


class Initializer:
    def setup(self):
        inject.clear_and_configure(configure_test)

        app.config['TESTING'] = True
        with app.test_client() as client:
            self.client = client


class TestUsers(Initializer):
    def test_create_new(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        assert resp.status_code == 201
        assert resp.json == {'user_id': 1}

        resp = self.client.post(
            '/users',
            json={'name': 'King Kong'}
        )
        assert resp.json == {'user_id': 2}

    def test_successful_get_user(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        user_id = resp.json['user_id']
        resp = self.client.get(f'/users/{user_id}')
        assert resp.status_code == 200
        assert resp.json == {'name': 'John Doe'}

    def test_get_unexistent_user(self):
        resp = self.client.get(f'/users/1')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 1'}

    def test_successful_update_user(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        user_id = resp.json['user_id']
        resp = self.client.put(
            f'/users/{user_id}',
            json={'name': 'Johanna Doe'}
        )
        assert resp.status_code == 200
        assert resp.json == {'status': 'success'}

    def test_unexistent_update_user(self):
        resp = self.client.put(
            f'/users/1',
            json={'name': 'Johanna Doe'}
        )
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 1'}


class TestGoods(Initializer):
    def test_create_goods(self):
        resp = self.client.post(
            '/goods',
            json=[{'name': 'Chocolate_bar', 'price': 10},
                  {'name': 'Snickers', 'price': 19},
                  {'name': 'Mars', 'price': 9.5},
                  {'name': 'Kinder_Chocolate', 'price': 26},
                  {'name': 'Nesquik', 'price': 25},
                  {'name': 'Bounty', 'price': 11.2},
                  {'name': 'Twix', 'price': 9.3},
                  {'name': 'Milky_Way', 'price': 10},
                  {'name': 'Milka&Daim', 'price': 20},
                  {'name': 'M&Ms', 'price': 21}]
        )
        assert resp.status_code == 201
        assert resp.json == {'goods_id': 1}
        resp = self.client.post(
            '/goods',
            json={'name': 'Olenka', 'price': 15}
        )
        assert resp.status_code == 201
        assert resp.json == {'goods_id': 2}

    def test_get_goods(self):
        resp = self.client.post(
            '/goods',
            json={'name': 'Chocolate_bar', 'price': 10, 'goods_id': 1}
        )
        goods_id = resp.json['goods_id']
        resp = self.client.get(f'/goods/{goods_id}')
        assert resp.status_code == 200
        assert resp.json == {'name': 'Chocolate_bar', 'price': 10, 'goods_id': 1}

    def test_update_goods(self):
        resp = self.client.post(
            '/goods',
            json={'name': 'Chocolate_bar', 'price': 10, 'goods_id': 1}
        )
        goods_id = resp.json['goods_id']
        resp = self.client.put(f'/goods/{goods_id}',
                               json={'name': 'Chocolate_bar', 'price': 1, 'goods_id': 1})
        assert resp.status_code == 200
        assert resp.json == {'successfully_updated': 1}


class TestStore(Initializer):
    def test_create_store(self):
        resp = self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 2}
        )
        assert resp.status_code == 201
        assert resp.json == {'store_id': 1}

        resp = self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Kiev', 'manager_id': 3}
        )
        assert resp.json == {'store_id': 2}

    def test_successful_get_store(self):
        resp = self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 2}
        )
        store_id = resp.json['store_id']
        resp = self.client.get(f'/store/{store_id}')
        assert resp.status_code == 200
        assert resp.json == {'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 2}

    def test_get_unexistent_store(self):
        resp = self.client.get(f'/store/1')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such store_id 1'}

    def test_successful_update_store(self):
        resp = self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 2}
        )
        store_id = resp.json['store_id']
        resp = self.client.put(
            f'/store/{store_id}',
            json={'name': 'Lazy Cat', 'location': 'Lviv', 'manager_id': 2}
        )
        assert resp.status_code == 200
        assert resp.json == {'status': 'success'}

    def test_unexistent_update_store(self):
        resp = self.client.put(
            f'/store/1',
            json={'name': 'Lazy Cat', 'location': 'Lviv', 'manager_id': 2}
        )
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such store_id 1'}


