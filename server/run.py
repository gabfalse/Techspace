from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT", 3306)),
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/")
def home():
    return jsonify({"message": "Server is running ✅"})

@app.route("/messages", methods=["GET"])
def get_messages():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM messages ORDER BY id DESC")
            rows = cursor.fetchall()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/messages", methods=["POST"])
def post_message():
    try:
        data = request.get_json()
        name = data.get("name")
        message = data.get("message")

        if not name or not message:
            return jsonify({"error": "name and message are required"}), 400

        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO messages (name, message) VALUES (%s, %s)", 
                (name, message)
            )
            conn.commit()
        conn.close()
        return jsonify({"status": "success", "name": name, "message": message})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
