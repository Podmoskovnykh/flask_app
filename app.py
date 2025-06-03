from flask import Flask
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="mydatabase",
        user="postgres",
        password="password"
    )
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT version();")
    version_row = cur.fetchone()
    cur.close()
    conn.close()

    # Извлекаем только "PostgreSQL X.Y"
    full_version = version_row[0]
    pg_version = full_version.split(' on ')[0]  # Отсекаем всё лишнее

    return f'Hello, Docker! Версия PostgreSQL: {pg_version}'

if __name__ == '__main__':
    app.run()
