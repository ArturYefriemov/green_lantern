import csv


def get_users():
    with open('users.csv', 'r') as f:
        reader = csv.DictReader(f)
        users = [user for user in reader]
    return users


def get_stores():
    with open('stores.csv', 'r') as s:
        reader = csv.DictReader(s)
        stores = [store for store in reader]
    return stores


def get_goods():
    with open('goods.csv', 'r') as g:
        reader = csv.DictReader(g)
        goods = [good for good in reader]
    return goods

