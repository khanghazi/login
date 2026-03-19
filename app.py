from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

FILE = "users.json"

# file create agar exist na kare
if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump([], f)

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    # purana data load karo
    with open(FILE, "r") as f:
        users = json.load(f)

    # new user add karo
    users.append({
        "email": email,
        "password": password
    })

    # save karo
    with open(FILE, "w") as f:
        json.dump(users, f, indent=4)

    print("New Login:", email, password)

    return jsonify({
        "status": "success",
        "message": "Login successful"
    })

if __name__ == "__main__":
    app.run(debug=True)