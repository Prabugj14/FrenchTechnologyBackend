from flask import Blueprint, jsonify

space = Blueprint("space", __name__)


@space.route("/api/space")
def space_info():
    return jsonify({
        "title": "Space Technology in France",
        "organization": "CNES",
        "country": "France",
        "launch_site": "Guiana Space Centre",
        "technology": "Ariane launch vehicles",
        "description": "France plays an important role in European space technology and space research.",
        "important_points": [
            "CNES is France's national space agency.",
            "The Guiana Space Centre is an important European spaceport.",
            "Ariane launch vehicles are used for European space missions."
        ]
    })