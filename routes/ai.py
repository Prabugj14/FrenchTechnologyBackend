from flask import Blueprint, jsonify

ai = Blueprint("ai", __name__)


@ai.route("/api/ai")
def artificial_intelligence():
    return jsonify({
        "title": "Artificial Intelligence in France",
        "concept": "Present the French AI ecosystem through companies, open science, research infrastructure and sovereign computing.",
        "goal": "Help visitors understand how French AI combines foundation models, collaborative platforms, open research and national computing infrastructure.",
        "description": (
            "France is developing artificial intelligence through research institutions, startups, open-source projects and public investment."
        ),
        "focus": [
            "Open science",
            "Digital sovereignty",
            "Ethical AI",
            "AI research",
            "Generative AI"
        ],
        "organizations": [
            {
                "name": "CNRS",
                "description": "A major French research organisation."
            },
            {
                "name": "Inria",
                "description": "A French research institute focused on digital sciences and technology."
            }
        ],
        "companies_and_labs": [
            {
                "name": "Mistral AI",
                "headline": "Europe's Answer to Silicon Valley Frontier AI",
                "core_ecosystem": "Paris-based generative AI and open-weight models",
                "description": (
                    "Mistral AI is presented in the project material as a major French AI company whose open-weight approach allows developers to download, modify and build on its models."
                ),
                "key_points": [
                    "Mistral Large",
                    "Codestral for coding",
                    "Mixtral with a sparse Mixture-of-Experts architecture",
                    "Open-weight model philosophy"
                ],
                "links": [
                    {
                        "label": "Official website",
                        "url": "https://mistral.ai/"
                    }
                ]
            },
            {
                "name": "Hugging Face",
                "headline": "The Global Collaborative Platform for Machine Learning",
                "core_ecosystem": "Open-source AI community and model hosting",
                "description": (
                    "The project material describes Hugging Face as a platform founded by French entrepreneurs that became a major hub for open-source machine-learning models, datasets and applications."
                ),
                "key_points": [
                    "Models and datasets",
                    "Transformers Python library",
                    "Open-source machine-learning ecosystem"
                ],
                "links": [
                    {
                        "label": "Official website",
                        "url": "https://huggingface.co/"
                    }
                ]
            },
            {
                "name": "Kyutai",
                "headline": "Democratizing AI with Non-Profit Open Science",
                "core_ecosystem": "Independent AI research laboratory",
                "description": (
                    "The project material presents Kyutai as a privately funded, non-profit open-science AI research laboratory working on multimodal AI and releasing research resources openly."
                ),
                "key_points": [
                    "Moshi real-time speech-to-speech AI",
                    "MoshiVis multimodal work",
                    "Open research and model access"
                ],
                "links": [
                    {
                        "label": "Official website",
                        "url": "https://kyutai.org/"
                    }
                ]
            }
        ],
        "infrastructure": [
            {
                "name": "Jean Zay supercomputer",
                "description": "A French high-performance computing system operated by CNRS and optimized for AI workloads.",
                "links": [
                    {
                        "label": "Jean Zay presentation",
                        "url": "http://www.idris.fr/en/docs/jean-zay/jean-zay/jean-zay-presentation/"
                    }
                ]
            },
            {
                "name": "AI Factory France",
                "description": "A government-backed ecosystem designed to provide startups and universities with access to high-performance computing, data spaces and expert support."
            },
            {
                "name": "Alice Recoque",
                "description": "The project material identifies Alice Recoque as a planned exascale computing system for next-generation AI workloads."
            }
        ]
    })
