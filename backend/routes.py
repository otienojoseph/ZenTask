from app import app, db
from flask import request, jsonify
from models import Users, Tasks, Sessions, Goals, Moods


# Users routes
@app.route("/api/users", methods=["GET"])
def user_list():
    users = db.session.execute(db.select(Users).order_by(Users.username)).scalars()
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
        password = data.get("password")

        new_user = Users(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
        )

        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_json()), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/users/<int:id>", methods=["GET"])
def user_detail(id):
    try:
        user = db.session.execute(db.select(Users).where(Users.user_id == id)).scalar()
        if user is None:
            return jsonify({"error": "User not found"}), 404

        return jsonify(user.to_json()), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/users/<int:id>", methods=["DELETE"])
def user_delete(id):
    try:
        user = db.session.execute(db.select(Users).where(Users.user_id == id)).scalar()
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
        user = db.session.execute(db.select(Users).where(Users.user_id == id)).scalar()
        if user is None:
            return jsonify({"error": "User not found"}), 404

        data = request.json

        for key, value in data.items():
            if hasattr(user, key):
                setattr(user, key, value)

        db.session.commit()
        return jsonify(user.to_json()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# Tasks routes
@app.route("/api/tasks", methods=["GET"])
def tasks_list():
    tasks = db.session.execute(db.select(Tasks).order_by(Tasks.task_id)).scalars()
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
        task = db.session.execute(db.select(Tasks).where(Tasks.task_id == id)).scalar()
        if task is None:
            return jsonify({"error": "Task not found"}), 404

        return jsonify(task.to_json()), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/tasks/<int:id>", methods=["DELETE"])
def task_delete(id):
    try:
        task = db.session.execute(db.select(Tasks).where(Tasks.task_id == id)).scalar()
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
        task = db.session.execute(db.select(Tasks).where(Tasks.task_id == id)).scalar()
        if task is None:
            return jsonify({"error": "Task not found"}), 404

        data = request.json

        for key, value in data.items():
            if hasattr(task, key):
                setattr(task, key, value)

        db.session.commit()
        return jsonify(task.to_json()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# Sessions routes
@app.route("/api/sessions", methods=["GET"])
def session_list():
    sessions = db.session.execute(
        db.select(Sessions).order_by(Sessions.session_id)
    ).scalars()
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
        session = db.session.execute(
            db.select(Sessions).where(Sessions.session_id == id)
        ).scalar()
        if session is None:
            return jsonify({"error": "Session not found"}), 404

        return jsonify(session.to_json()), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/sessions/<int:id>", methods=["DELETE"])
def session_delete(id):
    try:
        session = db.session.execute(
            db.select(Sessions).where(Sessions.session_id == id)
        ).scalar()
        if session is None:
            return jsonify({"error": "Session not found"}), 404

        db.session.delete(session)
        db.session.commit()

        return jsonify({"msg": "Session deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route("/api/sessions/<int:id>", methods=["PATCH"])
def session_update(id):
    try:
        session = db.session.execute(
            db.select(Sessions).where(Sessions.session_id == id)
        ).scalar()
        if session is None:
            return jsonify({"error": "Session not found"}), 404

        data = request.json

        for key, value in data.items():
            if hasattr(session, key):
                setattr(session, key, value)

        db.session.commit()

        return jsonify(session.to_json()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# Goals routes
@app.route("/api/goals", methods=["GET"])
def goal_list():
    goals = db.session.execute(db.select(Goals).order_by(Goals.goal_id)).scalars()
    result = [goal.to_json() for goal in goals]
    return jsonify(result), 200


@app.route("/api/goals/create", methods=["POST"])
def goal_create():
    try:
        data = request.json

        required_fields = ["goal_type", "goal_status", "task_id"]

        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field {field}"}), 400

        goal_type = data.get("goal_type")
        goal_status = data.get("goal_status")
        task_id = data.get("task_id")

        new_goal = Goals(goal_type=goal_type, goal_status=goal_status, task_id=task_id)

        db.session.add(new_goal)
        db.session.commit()
        return jsonify(new_goal.to_json()), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/goals/<int:id>", methods=["GET"])
def goal_detail(id):
    try:
        goal = db.session.execute(db.select(Goals).where(Goals.goal_id == id)).scalar()
        if goal is None:
            return jsonify({"error": "Goal not found"}), 404

        return jsonify(goal.to_json()), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/goals/<int:id>", methods=["DELETE"])
def goal_delete(id):
    try:
        goal = db.session.execute(db.select(Goals).where(Goals.goal_id == id)).scalar()
        if goal is None:
            return jsonify({"error": "Goal not found"}), 404

        db.session.delete(goal)
        db.session.commit()

        return jsonify({"msg": "Goal deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route("/api/goals/<int:id>", methods=["PATCH"])
def goal_update(id):
    try:
        goal = db.session.execute(db.select(Goals).where(Goals.goal_id == id)).scalar()
        if goal is None:
            return jsonify({"error": "Goal not found"}), 404

        data = request.json

        for key, value in data.items():
            if hasattr(goal, key):
                setattr(goal, key, value)

        db.session.commit()
        return jsonify(goal.to_json()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# Moods routes
@app.route("/api/moods", methods=["GET"])
def mood_list():
    moods = db.session.execute(db.select(Moods).order_by(Moods.mood_id)).scalars()
    result = [mood.to_json() for mood in moods]
    return jsonify(result), 200


@app.route("/api/moods/create", methods=["POST"])
def mood_create():
    try:
        data = request.json

        required_fields = ["mood_status", "session_id"]

        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field {field}"}), 400

        mood_status = data.get("mood_status")
        session_id = data.get("session_id")

        new_mood = Moods(mood_status=mood_status, session_id=session_id)

        db.session.add(new_mood)
        db.session.commit()
        return jsonify(new_mood.to_json()), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/moods/<int:id>", methods=["GET"])
def mood_detail(id):
    try:
        mood = db.session.execute(db.select(Moods).where(Moods.mood_id == id)).scalar()
        if mood is None:
            return jsonify({"error": "Mood not found"}), 404

        return jsonify(mood.to_json()), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/moods/<int:id>", methods=["DELETE"])
def mood_delete(id):
    try:
        mood = db.session.execute(db.select(Moods).where(Moods.mood_id == id)).scalar()
        if mood is None:
            return jsonify({"error": "Mood not found"}), 404

        db.session.delete(mood)
        db.session.commit()

        return jsonify({"msg": "Mood deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route("/api/moods/<int:id>", methods=["PATCH"])
def mood_update(id):
    try:
        mood = db.session.execute(db.select(Moods).where(Moods.mood_id == id)).scalar()
        if mood is None:
            return jsonify({"error": "Mood not found"}), 404

        data = request.json

        for key, value in data.items():
            if hasattr(mood, key):
                setattr(mood, key, value)

        db.session.commit()
        return jsonify(mood.to_json()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
