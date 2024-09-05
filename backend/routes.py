from app import app, db
from flask import request, jsonify
from models import Users, Tasks, Sessions, Goals, Moods

# get all Users
@app.route("/api/users", methods=["GET"])
def get_users():
    users = Users.query.all()
    result = [user.to_json() for user in users]
    return jsonify(result), 200
