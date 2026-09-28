# 🇫🇷 French Technology Backend

Backend API for the **French Technology & Innovation PBL website**.

This project presents French technological innovation through topics such as Artificial Intelligence, Biotechnology, Deep Tech, Energy, Space Technology, Startups, TGV Technology, important people, and the innovation timeline.

## 🛠️ Technologies Used

- Python
- Flask
- Flask-CORS
- Gunicorn
- Git & GitHub
- Render

## 📁 Project Structure

```text
Feanch backend/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
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
```

## 🔗 API Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Backend home/status |
| `/api/technology` | French technology information |
| `/api/timeline` | Technology timeline |
| `/api/tgv` | TGV information |
| `/api/innovations` | French technological innovations |
| `/api/energy` | Energy technology |
| `/api/space` | Space technology |
| `/api/startups` | French startups |
| `/api/ai` | Artificial Intelligence in France |
| `/api/biotech` | Biotechnology in France |
| `/api/deep-tech` | Deep-tech information |
| `/api/innovation-map` | French innovation map information |
| `/api/french-words` | French technology-related words |
| `/api/people` | Important people in French technology |

## 🌐 Live Backend

The backend is deployed on **Render**.

### Base URL

https://frenchtechnologybackend.onrender.com

### API Base URL

https://frenchtechnologybackend.onrender.com/api

The backend is publicly accessible, so the frontend can communicate with it without the backend computer being switched on.

## 🔌 Frontend Connection

The frontend can connect to this backend using JavaScript `fetch()`.

### Example

```javascript
const API_BASE_URL = "https://frenchtechnologybackend.onrender.com";

fetch(`${API_BASE_URL}/api/technology`)
  .then(response => response.json())
  .then(data => console.log(data));
```

The frontend can use the same base URL for all the API endpoints.

For example:

```text
https://frenchtechnologybackend.onrender.com/api/ai

https://frenchtechnologybackend.onrender.com/api/biotech

https://frenchtechnologybackend.onrender.com/api/timeline

https://frenchtechnologybackend.onrender.com/api/space

https://frenchtechnologybackend.onrender.com/api/people
```

## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Prabugj14/FrenchTechnologyBackend.git
cd FrenchTechnologyBackend
```

### 2. Create a virtual environment

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the backend

```bash
python app.py
```

The backend will run locally at:

```text
http://127.0.0.1:5001
```

You can test an API endpoint:

```text
http://127.0.0.1:5001/api/technology
```

## 🚀 Render Deployment

The backend is deployed as a **Render Web Service** and is connected to this GitHub repository.

### Build Command

```text
pip install -r requirements.txt
```

### Start Command

```text
gunicorn app:app
```

### Deployment URL

```text
https://frenchtechnologybackend.onrender.com
```

## 👥 Project

This backend is part of a group PBL project on **French Technology and Innovation**.

The frontend and backend are separate parts of the same website.

The frontend communicates with this Flask backend through the API endpoints listed above.
