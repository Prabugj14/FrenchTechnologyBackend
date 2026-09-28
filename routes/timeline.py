from flask import Blueprint, jsonify

timeline = Blueprint("timeline", __name__)


@timeline.route("/api/timeline")
def timeline_info():

    events = [
        {
            "year": "1666",
            "event": "Académie des Sciences",
            "description": "The French Academy of Sciences was established."
        },
        {
            "year": "1751-1772",
            "event": "Encyclopédie",
            "description": "The Encyclopédie helped spread scientific and technical knowledge."
        },
        {
            "year": "1783",
            "event": "Montgolfier Brothers",
            "description": "The Montgolfier brothers demonstrated the first public hot-air balloon flight."
        },
        {
            "year": "1799",
            "event": "Nicolas Appert",
            "description": "Appert developed an early method of preserving food."
        },
        {
            "year": "1829",
            "event": "Braille",
            "description": "Louis Braille developed the Braille reading and writing system."
        },
        {
            "year": "1839",
            "event": "Daguerreotype",
            "description": "Louis Daguerre developed an early practical photographic process."
        },
        {
            "year": "1885",
            "event": "Pasteur Vaccine",
            "description": "Louis Pasteur developed a successful rabies vaccine."
        },
        {
            "year": "1895",
            "event": "Lumière Brothers",
            "description": "The Lumière brothers played a major role in the development of cinema."
        },
        {
            "year": "1903",
            "event": "Marie Curie",
            "description": "Marie Curie received the Nobel Prize in Physics."
        },
        {
            "year": "1909",
            "event": "Louis Blériot",
            "description": "Louis Blériot crossed the English Channel by airplane."
        },
        {
            "year": "1939",
            "event": "CNRS",
            "description": "The French National Centre for Scientific Research was created."
        },
        {
            "year": "1945",
            "event": "CEA",
            "description": "The French Alternative Energies and Atomic Energy Commission was created."
        },
        {
            "year": "1969",
            "event": "Concorde",
            "description": "The Concorde supersonic aircraft made its first flight."
        },
        {
            "year": "1974",
            "event": "Nuclear Strategy",
            "description": "France expanded its nuclear electricity programme."
        },
        {
            "year": "1981",
            "event": "TGV",
            "description": "The first TGV high-speed railway service opened between Paris and Lyon."
        },
        {
            "year": "1982",
            "event": "Minitel",
            "description": "France introduced the Minitel online information service."
        },
        {
            "year": "1996",
            "event": "Ariane 5",
            "description": "Ariane 5 became an important European launch vehicle."
        },
        {
            "year": "2013",
            "event": "La French Tech",
            "description": "The French Tech initiative was launched to support the startup ecosystem."
        },
        {
            "year": "2017",
            "event": "Station F",
            "description": "Station F opened in Paris as a major startup campus."
        },
        {
            "year": "2019",
            "event": "French Tech Visa",
            "description": "France developed the French Tech Visa to attract international technology talent."
        },
        {
            "year": "2021",
            "event": "France 2030",
            "description": "France announced a major investment programme for innovation and technology."
        },
        {
            "year": "2023",
            "event": "Mistral AI",
            "description": "Mistral AI was founded in Paris."
        }
    ]

    return jsonify(events)