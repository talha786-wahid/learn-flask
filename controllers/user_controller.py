from flask import Flask, request, send_file
from app import app  # Ensure this is correct; you might not need it if it's in the same file
from models.user_model import user_model
from models.auth_model import auth_model
import os
from datetime import datetime

obj = user_model()
auth = auth_model()


@app.route("/")
def index():
    return "HELLLO"

@app.route("/user/all")
@auth.token_auth()
def all_users():
    return obj.all_user_model()

@app.route("/user/add", methods=["POST"])
def add_user():
    return obj.add_user_model(request.form)

@app.route("/user/addmultiple", methods=["POST"])
def add_multiple_users():
    return obj.add_multiple_users_model(request.json)

@app.route("/user/delete/<id>", methods=["DELETE"])
def delete_user(id):
    return obj.delete_user_model(id)

@app.route("/user/update", methods=["PUT"])
def update_user():
    return obj.update_user_model(request.form)

@app.route("/user/patch", methods=["PATCH"])
def patch_user():
    return obj.patch_user_model(request.form)

@app.route("/user/login", methods=["POST"])
def user_login():
    auth_data = request.authorization
    return obj.user_login_model(auth_data['username'], auth_data['password'])

if __name__ == '__main__':
    app.run(debug=True)
