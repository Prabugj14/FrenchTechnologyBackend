from flask import Blueprint, jsonify, request

from routes.ai import AI_DATA
from routes.biotech import BIOTECH_DATA

search = Blueprint("search", __name__)


@search.route("/api/search")
def search_all():

    query = request.args.get("q", "").strip().lower()

    if not query:
        return jsonify({
            "error": "Missing search query",
            "message": "Use /api/search?q=mistral"
        }), 400

    results = []

    # Search AI
    for item in AI_DATA.get("companies_and_labs", []):

        text = (
            str(item.get("name", "")) + " " +
            str(item.get("headline", "")) + " " +
            str(item.get("description", "")) + " " +
            " ".join(item.get("key_points", []))
        ).lower()

        if query in text:

            results.append({
                "section": "ai",
                "name": item["name"],
                "category": item.get("category", ""),
                "description": item.get("description", ""),
                "image_url": item.get("image_url", ""),
                "image_alt": item.get("image_alt", ""),
                "tags": item.get("tags", []),
                "links": item.get("links", [])
            })

    # Search biotechnology
    for item in BIOTECH_DATA.get("companies", []):

        text = (
            str(item.get("name", "")) + " " +
            str(item.get("technology", "")) + " " +
            str(item.get("headline", "")) + " " +
            str(item.get("description", "")) + " " +
            " ".join(item.get("key_features", []))
        ).lower()

        if query in text:

            results.append({
                "section": "biotech",
                "name": item["name"],
                "category": "Biotechnology",
                "description": item.get("description", ""),
                "image_url": item.get("image_url", ""),
                "image_alt": item.get("image_alt", ""),
                "tags": item.get("tags", []),
                "links": item.get("links", [])
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
            {"name": "Technology", "endpoint": "/api/technology"},
            {"name": "Timeline", "endpoint": "/api/timeline"},
            {"name": "TGV", "endpoint": "/api/tgv"},
            {"name": "Innovations", "endpoint": "/api/innovations"},
            {"name": "Energy", "endpoint": "/api/energy"},
            {"name": "Space", "endpoint": "/api/space"},
            {"name": "Startups", "endpoint": "/api/startups"},
            {"name": "Artificial Intelligence", "endpoint": "/api/ai"},
            {"name": "Biotechnology", "endpoint": "/api/biotech"},
            {"name": "Deep Tech", "endpoint": "/api/deep-tech"},
            {"name": "Innovation Map", "endpoint": "/api/innovation-map"},
            {"name": "French Technology Words", "endpoint": "/api/french-words"},
            {"name": "Important People", "endpoint": "/api/people"}
        ]
    })


@search.route("/api/health")
def health():

    return jsonify({
        "status": "ok",
        "service": "French Technology Backend"
    })