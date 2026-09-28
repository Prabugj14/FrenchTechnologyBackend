🇫🇷 French Technology Backend

Backend API for the French Technology & Innovation PBL website.

The project presents French technological innovation through topics such as AI, biotechnology, deep tech, energy, space technology, startups, TGV technology, important people, and the innovation timeline.

🛠️ Technologies Used

Python

Flask

Flask-CORS

Gunicorn

Git & GitHub

Render (deployment)

📁 Project Structure

Feanch backend/
├── app.py
├── requirements.txt
├── .gitignore
└── routes/
    ├── __init__.py
    ├── main.py
    ├── technology.py
    ├── timeline.py
    ├── tgv.py
    ├── energy.py
    ├── spacetech.py
    ├── ai.py
    ├── biotech.py
    ├── deeptech.py
    ├── people.py
    ├── innovation_map.py
    ├── STARTUPS.py
    └── FRENCH_TECHN_INNOVATIONS.py

🔗 API Endpoints

Endpoint

Purpose

/

Backend home/status

/api/technology

French technology information

/api/timeline

Technology timeline

/api/tgv

TGV information

/api/innovations

French technological innovations

/api/energy

Energy technology

/api/space

Space technology

/api/startups

French startups

/api/ai

Artificial Intelligence in France

/api/biotech

Biotechnology in France

/api/deep-tech

Deep-tech information

/api/innovation-map

French innovation map information

/api/french-words

French technology-related words

/api/people

Important people in French technology

▶️ Run Locally

1. Clone the repository

git clone https://github.com/Prabugj14/FrenchTechnologyBackend.git
cd FrenchTechnologyBackend

2. Create a virtual environment

macOS/Linux:

python3 -m venv .venv
source .venv/bin/activate

Windows:

python -m venv .venv
.venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Start the Flask server

python app.py

The backend will run locally on:

http://127.0.0.1:5001

You can then test an API endpoint, for example:

http://127.0.0.1:5001/api/technology

🌐 Frontend Connection

The frontend can send requests to the backend API using fetch().

For local development:

const API_BASE_URL = "http://127.0.0.1:5001";

fetch(`${API_BASE_URL}/api/technology`)
  .then(response => response.json())
  .then(data => {
    console.log(data);
  });

After deployment, the frontend should replace the local address with the public Render URL.

Example:

const API_BASE_URL = "https://YOUR-SERVICE.onrender.com";

fetch(`${API_BASE_URL}/api/technology`)
  .then(response => response.json())
  .then(data => {
    console.log(data);
  });

🚀 Deployment

The backend can be deployed as a Web Service on Render.

Recommended Render settings:

Build Command

pip install -r requirements.txt

Start Command

gunicorn app:app

After deployment, Render provides a public URL that the frontend can use to access the API.

## 🌐 Backend Deployment

The backend is deployed using Render and is connected to the GitHub repository.

### Live Backend URL

https://frenchtechnologybackend.onrender.com

### API Base URL

https://frenchtechnologybackend.onrender.com/api

The frontend can connect to the backend using the API endpoints provided in this project.

### Example

```javascript
const API_BASE_URL = "https://frenchtechnologybackend.onrender.com";

fetch(`${API_BASE_URL}/api/technology`)
  .then(response => response.json())
  .then(data => console.log(data));

👥 Project

This backend is part of a group PBL project on French Technology and Innovation.

The frontend and backend are separate parts of the same website. The frontend communicates with this Flask backend through the API endpoints listed above.
