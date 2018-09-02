# http://flask.pocoo.org/docs/1.0/api/#api

# $ export FLASK_APP=flask_demo.py
# $ export FLASK_ENV=development
# $ flask run
# $ flask run -h <ip> -p <port>

# $ python -m flask run


from flask import Flask, request, jsonify
app = Flask(__name__)


@app.errorhandler(400)
def bad_json(error):
    return 'Error parsing JSON', 400



# no trailing slash, 404 if client includes
# if trailing slash and client does not include, redirect
@app.route('/hello')
def hello_world():
    #print(f"client's user-agent: {request.headers.get('user-agent')}")
    app.logger.debug(f"client's user-agent: {request.headers.get('user-agent')}")
    return 'Hello, World!'


# variable rules- string, int, float, path, uuid
@app.route('/user/<int:user_id>', methods=['POST', 'GET'])
def show_user(user_id):
    if request.method == 'POST':
        if request.json is None:
            abort(400)
        else:
            return jsonify(success=True), 201
    else:
        return jsonify(_id=user_id)

