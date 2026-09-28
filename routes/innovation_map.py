from flask import Blueprint, jsonify

innovation_map = Blueprint("innovation_map", __name__)


@innovation_map.route("/api/innovation-map")
def get_innovation_map():
    return jsonify({
        "title": "French Innovation Map",
        "description": "Major technology and innovation centres in France.",
        "cities": [
            {
                "id": 1,
                "city": "Paris / Saclay",
                "specialization": [
                    "Artificial Intelligence",
                    "Quantum Computing",
                    "Scientific Research"
                ],
                "description": "A major centre for research, technology and innovation."
            },
            {
                "id": 2,
                "city": "Toulouse",
                "specialization": [
                    "Aerospace",
                    "Space Technology"
                ],
                "description": "An important centre for aerospace and space technology."
            },
            {
                "id": 3,
                "city": "Grenoble",
                "specialization": [
                    "Semiconductors",
                    "Advanced Materials"
                ],
                "description": "Known for technology, research and advanced materials."
            },
            {
                "id": 4,
                "city": "Sophia Antipolis",
                "specialization": [
                    "Telecommunications",
                    "Information Technology"
                ],
                "description": "A major technology and innovation hub."
            },
            {
                "id": 5,
                "city": "Lyon",
                "specialization": [
                    "Biotechnology",
                    "Pharmaceuticals",
                    "Chemicals"
                ],
                "description": "An important centre for biotechnology and health technology."
            },
            {
                "id": 6,
                "city": "Nantes",
                "specialization": [
                    "Digital Technology",
                    "Robotics"
                ],
                "description": "A growing centre for digital technology and robotics."
            },
            {
                "id": 7,
                "city": "Lille",
                "specialization": [
                    "Rail Technology",
                    "Logistics"
                ],
                "description": "A centre connected with rail, transport and logistics."
            }
        ]
    })