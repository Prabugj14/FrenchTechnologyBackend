from flask import Blueprint, jsonify

energy = Blueprint("energy", __name__)


@energy.route("/api/energy")
def energy_info():
    return jsonify({
        "title": "Nuclear Energy in France",
        "country": "France",
        "description": "Nuclear power is an important part of France's electricity system.",
        "facts": [
            "France has a large nuclear electricity programme.",
            "Nuclear power provides a major share of French electricity.",
            "France is developing future nuclear technologies."
        ]
    })