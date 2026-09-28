from flask import Blueprint, jsonify

biotech = Blueprint("biotech", __name__)


@biotech.route("/api/biotech")
def biotechnology():
    return jsonify({
        "title": "Biotechnology in France",

        "description": "France has an important biotechnology and health innovation ecosystem involving research institutions, startups and healthcare organisations.",

        "organizations": [
            {
                "name": "Inserm",
                "description": "French research organisation focused on health and medical research."
            },
            {
                "name": "Institut Pasteur",
                "description": "A major French research institution working in biology, medicine and infectious diseases."
            },
            {
                "name": "Paris-Saclay Cancer Cluster",
                "description": "A health and cancer research ecosystem."
            }
        ],

        "technologies": [
            "Cell and gene therapies",
            "AI diagnostics",
            "mRNA technology",
            "Artificial organs"
        ],

        "companies": [
            {
                "name": "CARMAT",
                "technology": "Aeson artificial heart"
            },
            {
                "name": "TreeFrog Therapeutics",
                "technology": "C-Stem cell therapy technology"
            },
            {
                "name": "DNA Script",
                "technology": "SYNTAX DNA synthesis technology"
            }
        ]
    })