from flask import Blueprint, jsonify

ai = Blueprint("ai", __name__)


@ai.route("/api/ai")
def artificial_intelligence():
    return jsonify({
        "title": "Artificial Intelligence in France",

        "description": "France is developing artificial intelligence through research institutions, startups, open-source projects and public investment.",

        "organizations": [
            {
                "name": "CNRS",
                "description": "A major French research organisation."
            },
            {
                "name": "Inria",
                "description": "A French research institute focused on digital sciences and technology."
            },
            {
                "name": "Hugging Face",
                "description": "A technology company and platform known for open-source machine learning models and tools."
            },
            {
                "name": "Mistral AI",
                "description": "A French AI company developing large language models and generative AI."
            },
            {
                "name": "Kyutai",
                "description": "A French AI research laboratory working on open science and AI research."
            }
        ],

        "infrastructure": [
            "Jean Zay supercomputer",
            "AI Factory France",
            "Future Alice Recoque exascale computing system"
        ],

        "focus": [
            "Open science",
            "Digital sovereignty",
            "Ethical AI",
            "AI research",
            "Generative AI"
        ]
    })