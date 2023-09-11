#!/usr/bin/python3
"""api to interact with the users table"""
from . import User
from . import storage
from flask import jsonify, request, abort
from . import app_views


@app_views.route('/<user_id_or_name>', strict_slashes=False)
def get_user(user_id_or_name):
    """
    gets a user(s) from database

    """
    user_info = user_id_or_name
    user = storage.get(User, name=user_info)

    if user is None or len(user) == 0:
        try:
            user =  storage.get(User, id=int(user_info))
        except ValueError:
            abort(404)
    if user is None:
        abort(404)
    if type(user).__name__ == "list":
        if len(user) == 1:
            return jsonify(user[0].to_dict())
        elif len(user) > 1:
            users = []
            for usr in user:
                users.append(usr.to_dict())
            return jsonify(users)
    return jsonify(user.to_dict())


@app_views.route('/', methods=['POST'], strict_slashes=False)
def add_user():
    """
    creates a new user
    """
    req = request.get_json()

    if req is None:
        abort(400, description="Not a json")
    if req.get('name') is None:
        abort(400, description="Missing name")
    if type(req.get('name')).__name__ != 'str':
        abort(400, description="name must be a string")
    user = User()
    user.name = req.get('name')
    user.save()
    return jsonify(user.to_dict()), 201


@app_views.route('/<user_id>', methods=['PUT', 'DELETE'], strict_slashes=False)
def update_or_delete_user(user_id):
    try:
        user = storage.get(User, id=int(user_id))
    except ValueError:
        abort(400, description="id has to be of type integer")
    if user is None:
        abort(404)

    if request.method == 'PUT':
        """
        updates a user
        """
        req = request.get_json()
        if req is None:
            abort(400, description="Not a json")
        if req.get('name') is None:
            abort(400, description="new name was not given")
        user.name = req['name']
        user.save()
        return jsonify(user.to_dict()), 201

    if request.method == 'DELETE':
        """
        deletes a user
        """
        storage.delete(user)
        storage.save()
        return jsonify({})
