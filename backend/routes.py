from app import app, db
from flask import request, jsonify
from models import Users, Tasks


# get all Users
@app.route("/api/users", methods=["GET"])
def user_list():
    users = Users.query.all()
    result = [user.to_json() for user in users]
    return jsonify(result), 200


@app.route("/api/users/create", methods=["POST"])
def user_create():
    try:
        data = request.json

        required_fields = ["first_name", "last_name", "username", "email"]

        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field {field}"}), 400

        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        email = data.get("email")

        new_user = Users(
            first_name=first_name, last_name=last_name, username=username, email=email
        )

        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_json()), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/users/<int:id>", methods=["GET"])
def user_detail(id):
    try:
        user = Users.query.get(id)
        if user is None:
            return jsonify({"error": "User not found"}), 404

        return jsonify(user.to_json()), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route("/api/users/<int:id>", methods=["DELETE"])
def user_delete(id):
    try:
        user = Users.query.get(id)
        if user is None:
            return jsonify({"error": "User not found"}), 404

        db.session.delete(user)
        db.session.commit()

        return jsonify({"msg": "User deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route("/api/users/<int:id>", methods=["PATCH"])
def user_update(id):
    try:
        user = Users.query.get(id)
        if user is None:
            return jsonify({"error": "User not found"}), 404

        data = request.json

        user.first_name = data.get("first_name", user.first_name)
        user.last_name = data.get("last_name", user.last_name)
        user.username = data.get("username", user.username)
        user.email = data.get("email", user.email)

        db.session.commit()
        return jsonify(user.to_json()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route("/api/tasks", methods=["GET"])
def tasks_list():
    tasks = Tasks.query.all()
    result = [task.to_json() for task in tasks]
    return jsonify(result), 200
