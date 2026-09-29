from flask import Flask, jsonify
from flask_cors import CORS

from routes.main import main
from routes.technology import technology
from routes.timeline import timeline
from routes.tgv import tgv
from routes.energy import energy
from routes.spacetech import space
from routes.STARTUPS import startups
from routes.ai import ai
from routes.biotech import biotech
from routes.deeptech import deeptech
from routes.people import important_people
from routes.innovation_map import innovation_map
from routes.search import search

app = Flask(__name__)

CORS(app)

app.register_blueprint(main)
app.register_blueprint(technology)
app.register_blueprint(timeline)
app.register_blueprint(tgv)
app.register_blueprint(energy)
app.register_blueprint(space)
app.register_blueprint(startups)
app.register_blueprint(ai)
app.register_blueprint(biotech)
app.register_blueprint(deeptech)
app.register_blueprint(important_people)
app.register_blueprint(innovation_map)
app.register_blueprint(search)


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({
        "error": "API endpoint not found",
        "message": "Please check the URL."
    }), 404


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5001,
        debug=True
    )