import pymysql
# [UPDATE] Tambahkan import DB_PORT
from config import DB_HOST, DB_USER, DB_PASS, DB_NAME, DB_PORT

print(f"Menghubungkan ke MySQL di {DB_HOST}:{DB_PORT}...")

conn = pymysql.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASS,
    port=DB_PORT
)

try:
    with conn.cursor() as cursor:
        print("Membaca file schema.sql...")
        with open('schema.sql', 'r') as f:
            sql_script = f.read()

        commands = sql_script.split(';')

        for command in commands:
            if command.strip():
                print(f"Eksekusi: {command[:40]}...") 
                cursor.execute(command)
        
        conn.commit()
        print("\n[SUKSES] Database techspace siap digunakan!")

except Exception as e:
    print(f"\n[ERROR] Terjadi kesalahan: {e}")

finally:
    conn.close()