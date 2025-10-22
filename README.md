# Techspace Community

Project ini adalah **web komunitas berbasis React (frontend) & Flask (backend)**.  
Fokus untuk membangun platform komunitas dengan fitur: showcase profile, latihan coding, dan pembelajaran web development.

## 🗂 Struktur Folder
Techspace/
├── server/ # Flask backend
│ ├── app/
│ │ ├── __pycache__/
│ │ ├── __init__.py
│ │ └── routes.py
│ ├── venv/
│ ├── requirements.txt
│ ├── config.py
│ ├── run.py
│ └── .env
└── client/ # React + Tailwind frontend
├── package.json
├── vite.config.js
├── src/
│ ├── Components/
│ ├── Pages/
│ │ └── Homepage.jsx
│ ├── App.jsx
│ ├── index.css
│ ├── main.jsx
└── index.html


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


