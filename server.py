import os
from flask import Flask, jsonify


DEV_KEY = os.getenv('REFUGEE_ROUTE_KEY')
app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(SECRET_KEY=DEV_KEY))


# Can move to class based views/routers as needed
@app.route('/', methods=['GET'])
def root():
    data = {'status': 200, 'message': 'OK!'}
    resp = jsonify(data)
    resp.status_code = 200
    return resp


if __name__ == '__main__':
    app.run(debug=True)
