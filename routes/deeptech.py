from flask import Blueprint, jsonify

deeptech = Blueprint("deeptech", __name__)


@deeptech.route("/api/deep-tech")
def deeptech_info():
    return jsonify({
        "title": "Deep Technology in France",

        "description": "Deep technology combines scientific research, advanced engineering and innovation to develop new technologies.",

        "main_areas": [
            {
                "id": 1,
                "name": "Artificial Intelligence",
                "description": "Advanced computer systems that can learn, analyse data and solve problems."
            },
            {
                "id": 2,
                "name": "Quantum Computing",
                "description": "A new type of computing based on principles of quantum physics."
            },
            {
                "id": 3,
                "name": "Biotechnology",
                "description": "Technology that uses biology and scientific research for healthcare and other applications."
            },
            {
                "id": 4,
                "name": "Robotics",
                "description": "Design and development of machines that can perform tasks automatically."
            },
            {
                "id": 5,
                "name": "Advanced Materials",
                "description": "Development of new materials with improved properties for technology and industry."
            }
        ],

        "applications": [
            "Healthcare",
            "Transport",
            "Energy",
            "Industry",
            "Scientific Research"
        ],

        "importance": [
            "Supports scientific research",
            "Creates new technological solutions",
            "Helps develop advanced industries",
            "Connects research with real-world applications"
        ],

        "french_focus": [
            "Research and development",
            "Innovation",
            "Digital technology",
            "Sustainable technology",
            "Industrial development"
        ]
    })