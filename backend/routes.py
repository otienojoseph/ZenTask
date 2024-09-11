from app import app, db
from flask import request, jsonify
from models import Users, Tasks, Sessions, Goals, Moods


# Users routes
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


# Tasks routes
@app.route("/api/tasks", methods=["GET"])
def tasks_list():
    tasks = Tasks.query.all()
    result = [task.to_json() for task in tasks]
    return jsonify(result), 200


@app.route("/api/tasks/create", methods=["POST"])
def task_create():
    try:
        data = request.json

        required_fields = ["title", "description", "priority"]

        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field {field}"}), 400

        title = data.get("title")
        description = data.get("description")
        priority = data.get("priority")
        user_id = data.get("user_id")
        session_id = data.get("session_id")
        goal_id = data.get("goal_id")

        new_task = Tasks(
            title=title,
            description=description,
            priority=priority,
            user_id=user_id,
            session_id=session_id,
            goal_id=goal_id,
        )

        db.session.add(new_task)
        db.session.commit()
        return jsonify(new_task.to_json()), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/tasks/<int:id>", methods=["GET"])
def task_detail(id):
    try:
        task = Tasks.query.get(id)
        if task is None:
            return jsonify({"error": "Task not found"}), 404

        return jsonify(task.to_json()), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/tasks/<int:id>", methods=["DELETE"])
def task_delete(id):
    try:
        task = Tasks.query.get(id)
        if task is None:
            return jsonify({"error": "Task not found"}), 404

        db.session.delete(task)
        db.session.commit()

        return jsonify({"msg": "Task deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route("/api/tasks/<int:id>", methods=["PATCH"])
def task_update(id):
    try:
        task = Tasks.query.get(id)
        if task is None:
            return jsonify({"error": "Task not found"}), 404

        data = request.json

        task.title = data.get("title")
        task.description = data.get("description")
        task.priority = data.get("priority")
        task.user_id = data.get("user_id")
        task.session_id = data.get("session_id")
        task.goal_id = data.get("goal_id")

        db.session.commit()
        return jsonify(task.to_json()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# Sessions routes
@app.route("/api/sessions", methods=["GET"])
def session_list():
    sessions = Sessions.query.all()
    result = [session.to_json() for session in sessions]
    return jsonify(result), 200


@app.route("/api/sessions/create", methods=["POST"])
def session_create():
    try:
        data = request.json

        required_fields = [
            "start_time",
            "end_time",
            "duration",
            "breaks",
            "task_id",
            "mood_id",
        ]

        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field {field}"}), 400

        start_time = data.get("start_time")
        end_time = data.get("end_time")
        duration = data.get("breaks")
        task_id = data.get("task_id")
        mood_id = data.get("mood_id")

        new_session = Sessions(
            start_time=start_time,
            end_time=end_time,
            duration=duration,
            task_id=task_id,
            mood_id=mood_id,
        )

        db.session.add(new_session)
        db.session.commit()
        return jsonify(new_session.to_json()), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/sessions/<int:id>", methods=["GET"])
def session_detail(id):
    try:
        session = Sessions.query.get(id)
        if session is None:
            return jsonify({"error": "Task not found"}), 404

        return jsonify(session.to_json()), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/sessions/<int:id>", methods=["DELETE"])
def session_delete(id):
    try:
        session = Sessions.query.get(id)
        if session is None:
            return jsonify({"error": "Task not found"}), 404

        db.session.delete(session)
        db.session.commit()

        return jsonify({"msg": "Task deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route("/api/sessions/<int:id>", methods=["PATCH"])
def session_update(id):
    try:
        session = Sessions.query.get(id)
        if session is None:
            return jsonify({"error": "Task not found"}), 404

        data = request.json

        session.start_time = data.get("start_time")
        session.end_time = data.get("end_time")
        session.duration = data.get("breaks")
        session.task_id = data.get("task_id")
        session.mood_id = data.get("mood_id")

        db.session.commit()
        return jsonify(session.to_json()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
