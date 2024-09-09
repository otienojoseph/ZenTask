from app import app, db
from flask import redirect, request, jsonify, url_for
from models import Users, Tasks, Sessions, Goals, Moods

# get all Users
@app.route("/api/users", methods=["GET"])
def user_list():
    # users = Users.query.all()
    # result = [user.to_json() for user in users]
    # return jsonify(result), 200
    users = db.session.execute(db.select(Users))
    return jsonify(users), 200

@app.route("/api/users/create", methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        user = Users(
            firs_tname = "Joseph",
            last_name = "Otieno",
            username = "Cruz",
            email = "otienoj.cruz@gmail.com"
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("User created!", id=user.id))
    
    return "user created"
