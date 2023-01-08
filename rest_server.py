from flask import Flask, request

from db_connector import add_user, get_user, delete_user, update_user

app = Flask(__name__)



# supported methods
@app.route('/data/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        add_user(user_id, user_name)
        if user is None:
            return {'status': 'error', 'reason': 'id already exists'}, 500  # status code
        return {'status': 'OK', 'user added': user_name}, 200  # status code

    elif request.method == 'GET':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        get_user(user_id)
        if user is None:
            return {'status': 'error', 'reason': 'no such id'}, 500  # status code
        return {'status': 'OK', 'user name': user_name}, 200  # status code

    elif request.method == 'PUT':
        # putting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.put('user_name')
        update_user(user_name, user_id)
        if user is None:
            return {'status': 'error', 'reason': 'no such id'}, 500  # status code
        return {'status': 'OK', 'user updated': user_name}, 200  # status code

    elif request.method == 'DELETE':
        # deleting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        delete_user(user_id)
        if user is None:
            return {'status': 'error', 'reason': 'no such id'}, 500  # status code
        return {'status': 'OK', 'user deleted': user_id}, 200  # status code


app.run(host='127.0.0.1', debug=True, port=5000)
