from flask import Flask
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="postgres.cjq4qqiagabn.ap-south-1.rds.amazonaws.com",
        database="postgres",
        user="postgres",
        password="postgres"
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM mytable;')
    results = cur.fetchall()
    cur.close()
    conn.close()
    return str(results)

@app.route('/health')
def health():
    return "Flask app is running!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
