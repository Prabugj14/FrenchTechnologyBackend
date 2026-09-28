from flask import Blueprint, jsonify

french_tech = Blueprint("french_tech", __name__)


@french_tech.route("/api/innovations")
def innovations():
    return jsonify([
        {
            "name": "Pascaline",
            "inventor": "Blaise Pascal",
            "year": "1642",
            "category": "Computing",
            "description": "An early mechanical calculator."
        },
        {
            "name": "Braille",
            "inventor": "Louis Braille",
            "year": "1829",
            "category": "Accessibility",
            "description": "A tactile writing system used by people who are blind or visually impaired."
        },
        {
            "name": "Rabies Vaccine",
            "inventor": "Louis Pasteur",
            "year": "1885",
            "category": "Medicine",
            "description": "A major development in modern vaccination."
        },
        {
            "name": "Cinema",
            "inventor": "Lumière Brothers",
            "year": "1895",
            "category": "Entertainment",
            "description": "The Lumière brothers made important contributions to early cinema."
        },
        {
            "name": "Concorde",
            "inventor": "French-British engineering teams",
            "year": "1969",
            "category": "Aerospace",
            "description": "A supersonic passenger aircraft."
        },
        {
            "name": "TGV",
            "inventor": "French railway engineering",
            "year": "1981",
            "category": "Transport",
            "description": "France's high-speed railway system."
        },
        {
            "name": "Minitel",
            "inventor": "France Télécom",
            "year": "1982",
            "category": "Communication",
            "description": "An early online information and communication service."
        },
        {
            "name": "Ariane",
            "inventor": "European space programme",
            "year": "1970s-",
            "category": "Space",
            "description": "A family of European launch vehicles."
        }
    ])