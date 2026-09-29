from flask import Blueprint, jsonify, request

search = Blueprint("search", __name__)


# Simple list used by the search feature
SEARCH_DATA = [
    {
        "name": "Mistral AI",
        "section": "AI",
        "keywords": [
            "mistral",
            "artificial intelligence",
            "generative ai",
            "open weight",
            "codestral",
            "mixtral"
        ],
        "endpoint": "/api/ai"
    },

    {
        "name": "Hugging Face",
        "section": "AI",
        "keywords": [
            "hugging face",
            "artificial intelligence",
            "machine learning",
            "open source",
            "models",
            "datasets"
        ],
        "endpoint": "/api/ai"
    },

    {
        "name": "Kyutai",
        "section": "AI",
        "keywords": [
            "kyutai",
            "artificial intelligence",
            "open science",
            "moshi",
            "speech to speech",
            "multimodal"
        ],
        "endpoint": "/api/ai"
    },

    {
        "name": "Jean Zay",
        "section": "AI",
        "keywords": [
            "jean zay",
            "supercomputer",
            "high performance computing",
            "hpc",
            "cnrs"
        ],
        "endpoint": "/api/ai"
    },

    {
        "name": "CARMAT",
        "section": "Biotechnology",
        "keywords": [
            "carmat",
            "artificial heart",
            "aeson",
            "heart",
            "medical technology",
            "biotechnology"
        ],
        "endpoint": "/api/biotech"
    },

    {
        "name": "TreeFrog Therapeutics",
        "section": "Biotechnology",
        "keywords": [
            "treefrog",
            "c-stem",
            "cell therapy",
            "stem cells",
            "3d cell culture",
            "biotechnology"
        ],
        "endpoint": "/api/biotech"
    },

    {
        "name": "DNA Script",
        "section": "Biotechnology",
        "keywords": [
            "dna script",
            "dna",
            "syntax",
            "enzymatic dna synthesis",
            "genomics",
            "biotechnology"
        ],
        "endpoint": "/api/biotech"
    }
]


@search.route("/api/search")
def search_all():

    query = request.args.get("q", "").strip().lower()

    if not query:
        return jsonify({
            "error": "Missing search query",
            "message": "Use /api/search?q=mistral"
        }), 400

    results = []

    for item in SEARCH_DATA:

        text = item["name"].lower() + " " + " ".join(item["keywords"])

        if query in text:

            results.append({
                "name": item["name"],
                "section": item["section"],
                "endpoint": item["endpoint"]
            })

    return jsonify({
        "query": query,
        "count": len(results),
        "results": results
    })


@search.route("/api/topics")
def topics():

    return jsonify({
        "topics": [
            {
                "name": "Technology",
                "endpoint": "/api/technology"
            },
            {
                "name": "Timeline",
                "endpoint": "/api/timeline"
            },
            {
                "name": "TGV",
                "endpoint": "/api/tgv"
            },
            {
                "name": "Innovations",
                "endpoint": "/api/innovations"
            },
            {
                "name": "Energy",
                "endpoint": "/api/energy"
            },
            {
                "name": "Space",
                "endpoint": "/api/space"
            },
            {
                "name": "Startups",
                "endpoint": "/api/startups"
            },
            {
                "name": "Artificial Intelligence",
                "endpoint": "/api/ai"
            },
            {
                "name": "Biotechnology",
                "endpoint": "/api/biotech"
            },
            {
                "name": "Deep Tech",
                "endpoint": "/api/deep-tech"
            },
            {
                "name": "Innovation Map",
                "endpoint": "/api/innovation-map"
            },
            {
                "name": "French Technology Words",
                "endpoint": "/api/french-words"
            },
            {
                "name": "Important People",
                "endpoint": "/api/people"
            }
        ]
    })


@search.route("/api/health")
def health():

    return jsonify({
        "status": "ok",
        "service": "French Technology Backend"
    })