from flask import Blueprint, render_template
from flask_login import current_user, login_required
from grocery_store.models import User


orders = Blueprint('orders', __name__)


@orders.route('/orders')
@login_required
def user_orders():
    if current_user:
        user = User.query.filter_by(user_id=current_user.user_id).first()
        order_list = []
        for order in current_user.orders:
            orders_data = {
                'store': order.store.name,
                'data': order.created_time,
                'price': sum([good.good.price for good in order.order_lines]),
                'goods': {good.good.name: good.good.price for good in order.order_lines},
                }
            order_list.append(orders_data)

    return render_template('orders.html',name=user, orders=order)
