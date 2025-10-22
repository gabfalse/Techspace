# Techspace Community

Project ini adalah **web komunitas berbasis React (frontend) & Flask (backend)**.  
Fokus untuk membangun platform komunitas dengan fitur: showcase profile, latihan coding, dan pembelajaran web development.

## 🗂 Struktur Folder
Techspace/ <br/>
├── server/ # Flask backend <br/>
│ ├── app/ <br/>
│ │ ├── __pycache__/ <br/>
│ │ ├── __init__.py <br/>
│ │ └── routes.py <br/>
│ ├── venv/ <br/>
│ ├── requirements.txt <br/>
│ ├── config.py <br/>
│ ├── run.py <br/>
│ └── .env <br/>
└── client/ # React + Tailwind frontend <br/>
├── package.json <br/>
├── vite.config.js <br/>
├── src/ <br/>
│ ├── Components/ <br/>
│ ├── Pages/ <br/>
│ │ └── Homepage.jsx <br/>
│ ├── App.jsx <br/>
│ ├── index.css <br/>
│ ├── main.jsx <br/>
└── index.html <br/>


---

## Persiapan & Instalasi

### 1. Backend (Flask)

1. Buat virtual environment (bash):
python -m venv venv

2. Aktifkan venv:
Windows:
venv\Scripts\activate
Mac/Linux:
source venv/bin/activate

3. Install dependencies:
pip install -r backend/requirements.txt

4. Jalankan backend:
cd server
py run.py

### 2. Frontend (React + Vite + Tailwind)
1. Masuk folder frontend:
cd client

3. Install dependencies:
pnpm install

4. Jalankan development server:
pnpm run dev

# Dependencies
Backend (Flask)
Flask==3.1.2
flask-cors==6.0.1
python-dotenv==1.1.1
PyMySQL==1.1.2
Blinker, Jinja2, Werkzeug, MarkupSafe, Click, Colorama, Itsdangerous

# Frontend (React + Tailwind + MUI)
react, react-dom
tailwindcss, @tailwindcss/vite
@mui/material, @emotion/react, @emotion/styled
Vite, ESLint, plugin-react


