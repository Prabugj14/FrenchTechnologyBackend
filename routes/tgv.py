from flask import Blueprint, jsonify

tgv = Blueprint("tgv", __name__)


@tgv.route("/api/tgv")
def tgv_info():
    return jsonify({
        "name": "TGV",
        "country": "France",
        "route": "Paris to Lyon",
        "speed": "320 km/h",
        "type": "High-Speed Train",
        "description": "The TGV is France's high-speed railway system."
    })