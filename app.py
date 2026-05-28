from flask import Flask, jsonify
from datetime import datetime
import socket

app = Flask(__name__)

APP_NAME = "AKS GitOps Demo App"


# Home API
@app.route("/")
def home():

    response = {
        "application": APP_NAME,
        "message": "Application deployed successfully using AKS + GitOps",
        "server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "hostname": socket.gethostname(),
        "status": "Running"
    }

    return jsonify(response)


# Health Check API
@app.route("/health")
def health():

    return jsonify({
        "status": "UP",
        "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


# About API
@app.route("/about")
def about():

    return jsonify({
        "project": "Azure Kubernetes Service GitOps Assignment",
        "technology": [
            "Python",
            "Flask",
            "Docker",
            "Kubernetes",
            "ArgoCD"
        ],
        "environment": "test"
    })


if __name__ == "__main__":

    print(f"Starting {APP_NAME}...")

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )