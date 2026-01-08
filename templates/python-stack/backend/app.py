from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import time

app = Flask(__name__)
CORS(app)

#Database connection
def get_db_connection():
    conn = psycopg2.connect(
        host='database',
        port=5432,
        user='postgres',
        password='postgres',
        database='hackstack'
    )
    return conn

#Initialize database
def init_db():
    retries = 5
    while retries > 0:
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('''
                CREATE TABLE IF NOT EXISTS items (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL
                )
            ''')
            conn.commit()
            cur.close()
            conn.close()
            print('Database initialized')
            break
        except Exception as e:
            print(f'Database connection failed, retrying... ({retries} left)')
            retries -= 1
            time.sleep(2)

init_db()

#Routes
@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'message': 'Backend is running!'})

@app.route('/api/items', methods=['GET'])
def get_items():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM items')
    items = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{'id': item[0], 'name': item[1]} for item in items])

@app.route('/api/items', methods=['POST'])
def create_item():
    data = request.json
    name = data.get('name')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO items (name) VALUES (%s) RETURNING id, name', (name,))
    item = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'id': item[0], 'name': item[1]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
