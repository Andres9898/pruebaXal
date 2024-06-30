from flask import Flask, jsonify
import mysql.connector
import requests

app = Flask(__name__)

# Configuración de la base de datos MySQL
db_config = {
    'host': 'localhost:3306',
    'user': 'root',
    'password': 'password',
    'database': 'test'
}

# Función para obtener una conexión a la base de datos
def get_db():
    return mysql.connector.connect(**db_config)

@app.route('/api/answered-unanswered', methods=['GET'])
def get_answered_unanswered():
    # Aquí va la lógica para obtener datos de StackExchange
    response = requests.get('https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow')
    data = response.json()

    answered = sum(1 for item in data['items'] if item['is_answered'])
    unanswered = len(data['items']) - answered

    return jsonify({'answered': answered, 'unanswered': unanswered})

@app.route('/api/highest-reputation', methods=['GET'])
def get_highest_reputation():
    # Aquí va la lógica para obtener datos de StackExchange
    response = requests.get('https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow')
    data = response.json()

    highest_reputation = max(data['items'], key=lambda item: item['owner']['reputation'])

    return jsonify(highest_reputation)

@app.route('/api/lowest-views', methods=['GET'])
def get_lowest_views():
    # Aquí va la lógica para obtener datos de StackExchange
    response = requests.get('https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow')
    data = response.json()

    lowest_views = min(data['items'], key=lambda item: item['view_count'])

    return jsonify(lowest_views)

@app.route('/api/oldest-newest', methods=['GET'])
def get_oldest_newest():
    # Aquí va la lógica para obtener datos de StackExchange
    response = requests.get('https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow')
    data = response.json()

    oldest = min(data['items'], key=lambda item: item['creation_date'])
    newest = max(data['items'], key=lambda item: item['creation_date'])

    return jsonify({'oldest': oldest, 'newest': newest})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
