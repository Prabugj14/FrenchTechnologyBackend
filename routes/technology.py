from flask import Blueprint, jsonify

technology = Blueprint("technology", __name__)


@technology.route("/api/technology")
def technology_info():
    return jsonify({
        "title": "French Technology and Innovation",
        "country": "France",
        "description": "France has a strong history of scientific research, engineering and technological innovation.",
        "main_areas": [
            "Artificial Intelligence",
            "Biotechnology",
            "Quantum Computing",
            "Space Technology",
            "Sustainable Technology"
        ]
    })