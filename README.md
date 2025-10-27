# Techspace Community

Project ini adalah **web komunitas berbasis React (frontend) & Flask (backend)**.   <br/>
Fokus untuk membangun platform komunitas dengan fitur: showcase profile, latihan coding, dan pembelajaran web development. <br/>

---

## Persiapan & Instalasi

### 1. Backend (Flask) <br/>

1. Buat virtual environment (bash): <br/>
python -m venv venv <br/>

2. Aktifkan venv: <br/>
Windows: <br/>
venv\Scripts\activate <br/>
Mac/Linux: <br/>
source venv/bin/activate <br/>

3. Install dependencies: <br/>
pip install -r backend/requirements.txt <br/>

4. Jalankan backend: <br/>
cd server <br/>
py app.py <br/>

### 2. Frontend (React + Vite + Tailwind) <br/>
1. Masuk folder frontend: <br/>
cd client <br/>

3. Install dependencies: <br/>
pnpm install <br/>

4. Jalankan development server: <br/>
pnpm run dev <br/>

# Dependencies <br/>
Backend (Flask) <br/>
Flask==3.1.2 <br/>
flask-cors==6.0.1 <br/>
python-dotenv==1.1.1 <br/>
PyMySQL==1.1.2 <br/>
Blinker, Jinja2, Werkzeug, MarkupSafe, Click, Colorama, Itsdangerous <br/>

# Frontend (React + Tailwind + MUI) <br/>
react, react-dom <br/>
tailwindcss, @tailwindcss/vite <br/>
@emotion/react, @emotion/styled <br/>
Vite, ESLint, plugin-react <br/>


