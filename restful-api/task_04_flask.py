#!/usr/bin/python3
"""A simple Flask API that stores users in memory and serves them as JSON."""
from flask import Flask, jsonify, request


app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """Return a welcome message for the root URL."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_usernames():
    """Return a JSON list of every username stored in the API."""
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route("/status")
def status():
    """Return OK to show that the API is running."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Return the full user object for a username, or a 404 error."""
    user = users.get(username)

    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user from the JSON request body and return it."""
    data = request.get_json(silent=True)

    if data is None or not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data

    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()