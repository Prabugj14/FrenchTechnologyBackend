from flask import Blueprint, jsonify

startups = Blueprint("startups", __name__)


@startups.route("/api/startups")
def startups_info():
    return jsonify({
        "title": "French Startup Ecosystem",

        "organizations": [
            {
                "name": "La French Tech",
                "description": "A French initiative supporting the technology startup ecosystem."
            },
            {
                "name": "Station F",
                "description": "A major startup campus located in Paris."
            }
        ],

        "companies": [
            "BlaBlaCar",
            "Doctolib",
            "Deezer",
            "OVHcloud",
            "Back Market",
            "Qonto",
            "Ledger",
            "PayFit",
            "Mistral AI",
            "Hugging Face"
        ]
    })