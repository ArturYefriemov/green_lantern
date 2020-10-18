import json
import requests
from flask import jsonify, Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def send_data():
    posted_file = str(requests.files['data.txt'].read(), 'utf-8')
    posted_data = json.load(requests.files['data.json'])
    print(posted_file)
    print(posted_data)
    return '{}\n{}\n'.format(posted_file, posted_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
