from flask import Blueprint, jsonify

biotech = Blueprint("biotech", __name__)

BIOTECH_DATA = {

    "title": "Biotechnology in France",
    "country": "France",

    "concept": (
        "France connects public biomedical research, deep-tech startups and "
        "healthcare innovation to turn scientific ideas into practical technologies."
    ),

    "goal": (
        "Show how French biotechnology links research institutions, engineering "
        "and startups in areas such as artificial organs, cell therapy and DNA synthesis."
    ),

    "description": (
        "France is rapidly transforming its scientific legacy into a biotechnology "
        "hub. The ecosystem combines public research, government-backed innovation "
        "and commercial deep-tech."
    ),

    "overview": {

        "development": (
            "The ecosystem connects institutions such as Inserm and Institut Pasteur "
            "with commercial spin-offs. Bioclusters such as the Paris-Saclay Cancer "
            "Cluster bring researchers, clinicians and investment closer together."
        ),

        "impact": (
            "French biotech focuses on areas including cell and gene therapies, "
            "AI-driven diagnostics and mRNA technology, while also supporting "
            "sustainability-oriented biological solutions."
        ),

        "usefulness_in_action": (
            "The infrastructure turns complex biology into practical technology: "
            "artificial-organ replacement, scalable cell-therapy manufacturing "
            "and local DNA synthesis."
        )
    },

    "technologies": [
        "Cell and gene therapies",
        "AI-driven diagnostics",
        "mRNA technology",
        "Artificial organs",
        "Enzymatic DNA synthesis"
    ],

    "organizations": [

        {
            "name": "Inserm",
            "description": (
                "French research organisation focused on health and medical research."
            ),
            "image_url": "",
            "image_alt": "Inserm visual"
        },

        {
            "name": "Institut Pasteur",
            "description": (
                "A major French research institution working in biology, medicine "
                "and infectious diseases."
            ),
            "image_url": "",
            "image_alt": "Institut Pasteur visual",

            "links": [
                {
                    "label": "Official website",
                    "url": "https://www.pasteur.fr/en"
                }
            ]
        },

        {
            "name": "Paris-Saclay Cancer Cluster",
            "description": (
                "A health and cancer research ecosystem bringing researchers, "
                "clinicians and innovation partners together."
            ),
            "image_url": "",
            "image_alt": "Paris-Saclay Cancer Cluster visual"
        }
    ],

    "companies": [

        {
            "name": "CARMAT",
            "technology": "Aeson® Total Artificial Heart",
            "headline": "Engineering the Aeson® Total Artificial Heart",

            "description": (
                "CARMAT developed the Aeson® artificial heart at the intersection "
                "of medical and aerospace engineering. Its design targets advanced "
                "biventricular heart failure and combines an implantable prosthesis "
                "with a portable external power and control system."
            ),

            "key_features": [
                "Hemocompatibility using bioprosthetic materials in blood-contacting areas",
                "Pulsatile pumping designed to reproduce systolic and diastolic phases",
                "Autoregulation using embedded electronics, sensors and microprocessors",
                "Portable external controller and battery system"
            ],

            "technical_details": {

                "implantable_system": [
                    "Two ventricles",
                    "Two electrohydraulic rotary pumps",
                    "Embedded electronics",
                    "Flexible hybrid membranes",
                    "Four bioprosthetic valves"
                ],

                "external_system_weight_kg": 4,
                "battery_life_hours_at_6_lpm": 4
            },

            "milestones": [

                {
                    "year": 2020,
                    "event": (
                        "CE marking obtained for Aeson® for the "
                        "bridge-to-transplant indication."
                    )
                },

                {
                    "year": 2021,
                    "event": "First sales in Europe."
                },

                {
                    "year": 2021,
                    "event": (
                        "Temporary voluntary suspension of implants following "
                        "identified quality issues."
                    )
                },

                {
                    "year": 2022,
                    "event": (
                        "Sales resumed in Europe after the required regulatory steps."
                    )
                }
            ],

            "image_url": "",
            "image_alt": "CARMAT Aeson artificial heart visual",

            "tags": [
                "Biotech",
                "Medical Technology",
                "Artificial Heart"
            ],

            "links": [

                {
                    "label": "CARMAT website",
                    "url": "https://www.carmatsa.com/"
                },

                {
                    "label": "CARMAT video",
                    "url": "https://www.youtube.com/watch?v=xdcLKTpxr2g"
                }
            ],

            "source_note": (
                "Technical details are based on the CARMAT 2022 Universal "
                "Registration Document supplied for the project."
            )
        },

        {
            "name": "TreeFrog Therapeutics",
            "technology": "C-Stem™ Technology",
            "headline": "Scaling Cell Therapy with 3D Microencapsulation",

            "description": (
                "TreeFrog Therapeutics uses microfluidic technology to encapsulate "
                "stem cells in protective alginate shells, supporting 3D growth "
                "instead of flat 2D culture."
            ),

            "key_features": [
                "Biomimetic porous alginate capsules",
                "3D cell growth environment",
                "Scalable cell-therapy manufacturing"
            ],

            "image_url": "",
            "image_alt": "TreeFrog cell therapy visual",

            "tags": [
                "Biotech",
                "Cell Therapy",
                "3D Cell Culture"
            ],

            "links": [
                {
                    "label": "Official website",
                    "url": "https://treefrog.fr/"
                }
            ]
        },

        {
            "name": "DNA Script",
            "technology": "Enzymatic DNA Synthesis (EDS) and SYNTAX™ System",
            "headline": "On-Demand DNA Synthesis",

            "description": (
                "DNA Script develops benchtop DNA synthesis technology that uses "
                "engineered enzymes to create DNA sequences directly in the laboratory."
            ),

            "key_features": [
                "Enzymatic DNA synthesis",
                "Benchtop SYNTAX™ system",
                "On-demand DNA and RNA sequence production"
            ],

            "applications": [
                "Rapid diagnostics",
                "Targeted cancer-therapy research",
                "mRNA vaccine development"
            ],

            "image_url": "",
            "image_alt": "DNA Script SYNTAX visual",

            "tags": [
                "Biotech",
                "DNA",
                "Genomics"
            ],

            "links": [
                {
                    "label": "Project video",
                    "url": "https://www.youtube.com/watch?v=QxOy9QLdBRA"
                }
            ]
        }
    ]
}


@biotech.route("/api/biotech")
def biotechnology():
    return jsonify(BIOTECH_DATA)