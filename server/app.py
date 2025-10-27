from flask import Flask, jsonify
from flask_cors import CORS
from config import get_db_connection  # sudah ada di config.py

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    try:
        conn = get_db_connection()
        conn.close()
        return jsonify({"message": "Server is running ✅", "db_status": "Connected ✅"})
    except Exception as e:
        return jsonify({"message": "Server is running ✅", "db_status": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
