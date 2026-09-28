from flask import Blueprint, jsonify

important_people = Blueprint("important_people", __name__)


@important_people.route("/api/people")
def get_people():
    return jsonify({
        "title": "Important People in French Science and Technology",
        "description": "Scientists, inventors and innovators connected with French science and technology.",
        "people": [
            {
                "id": 1,
                "name": "Blaise Pascal",
                "field": "Mathematics and Computing",
                "contribution": "Pascaline mechanical calculator",
                "year": "1642"
            },
            {
                "id": 2,
                "name": "Louis Braille",
                "field": "Accessibility",
                "contribution": "Braille writing system",
                "year": "1829"
            },
            {
                "id": 3,
                "name": "Louis Pasteur",
                "field": "Medicine and Microbiology",
                "contribution": "Vaccination and microbiology",
                "year": "1885"
            },
            {
                "id": 4,
                "name": "Marie Curie",
                "field": "Physics and Chemistry",
                "contribution": "Research on radioactivity",
                "year": "1903"
            },
            {
                "id": 5,
                "name": "Louis Blériot",
                "field": "Aviation",
                "contribution": "Early aviation achievements",
                "year": "1909"
            },
            {
                "id": 6,
                "name": "Arthur Mensch",
                "field": "Artificial Intelligence",
                "contribution": "Co-founder of Mistral AI",
                "year": "2023"
            }
        ]
    })