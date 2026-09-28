from flask import Blueprint, jsonify

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return jsonify({
        "message": "Bienvenue! Welcome to the French Technology Website.",
        "status": "Backend is running",
        "project": "French Technology and Innovation",
        "language": "French and English"
    })


@main.route("/api")
def api_home():
    return jsonify({
        "message": "French Technology API",
        "available_endpoints": [
            "/api/technology",
            "/api/timeline",
            "/api/tgv",
            "/api/innovations",
            "/api/energy",
            "/api/space",
            "/api/startups",
            "/api/ai",
            "/api/biotech",
            "/api/deep-tech",
            "/api/innovation-map",
            "/api/french-words",
            "/api/people"
        ]
    })