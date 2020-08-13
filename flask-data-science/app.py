import os

from flask import Flask, request, jsonify, abort, redirect, url_for, render_template
from markupsafe import escape
import joblib
import numpy as np
from werkzeug.utils import secure_filename

from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import DataRequired

app = Flask(__name__)

knn = joblib.load('knn.joblib')


@app.route('/')
def hello():
    print(1 + 2)
    return 'Hello my very best friend!!!!'


@app.route('/user/<username>')
def show_user_profile(username):
    username = float(username) ** 2
    return 'User %s' % escape(username)


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


@app.route('/avg/<nums>')
def avg(nums):
    nums = nums.split(',')
    nums = [float(num) for num in nums]
    nums_mean = mean(nums)
    print(nums_mean)
    return str(nums_mean)


@app.route('/iris/<param>')
def iris(param):
    try:
        param = param.split(',')
        param = [float(num) for num in param]

        param = np.array(param).reshape(1, -1)
        predict = knn.predict(param)

        return str(predict)
    except ValueError:
        return redirect(url_for('bad_request'))


@app.route('/show_img')
def show_image():
    return '<img src="/static/Irissetosa1.jpg" alt="Flower">'


@app.route('/badrequest400')
def bad_request():
    return abort(400)


@app.route('/iris_post', methods=['POST'])
def add_message():
    try:
        content = request.get_json()

        param = content['flower'].split(',')
        param = [float(num) for num in param]

        param = np.array(param).reshape(1, -1)
        predict = knn.predict(param)

        predict = {'class': str(predict[0])}
    except ValueError:
        return redirect(url_for('bad_request'))

    return jsonify(predict)


app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))


class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    file = FileField()


@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        print(form.name.data)

        f = form.file.data
        filename = form.name.data + '.txt'
        f.save(os.path.join(
            filename
        ))

        return ('form submmited')
    return render_template('submit.html', form=form)
