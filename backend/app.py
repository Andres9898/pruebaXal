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

# Conexión a la base de datos MySQL
mydb = mysql.connector.connect(
    host=db_config['host'],
    user=db_config['user'],
    password=db_config['password'],
    database=db_config['database']
)

# Cursor para ejecutar consultas
mycursor = mydb.cursor(dictionary=True)

# Endpoints para consumir datos de StackExchange
@app.route('/api/answered-unanswered', methods=['GET'])
def get_answered_unanswered():
    response = requests.get('https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow')
    data = response.json()

    answered = sum(1 for item in data['items'] if item['is_answered'])
    unanswered = len(data['items']) - answered

    return jsonify({'answered': answered, 'unanswered': unanswered})

@app.route('/api/highest-reputation', methods=['GET'])
def get_highest_reputation():
    response = requests.get('https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow')
    data = response.json()

    highest_reputation = max(data['items'], key=lambda item: item['owner']['reputation'])

    return jsonify(highest_reputation)

@app.route('/api/lowest-views', methods=['GET'])
def get_lowest_views():
    response = requests.get('https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow')
    data = response.json()

    lowest_views = min(data['items'], key=lambda item: item['view_count'])

    return jsonify(lowest_views)

@app.route('/api/oldest-newest', methods=['GET'])
def get_oldest_newest():
    response = requests.get('https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow')
    data = response.json()

    oldest = min(data['items'], key=lambda item: item['creation_date'])
    newest = max(data['items'], key=lambda item: item['creation_date'])

    return jsonify({'oldest': oldest, 'newest': newest})

# Consultas SQL para datos de vuelos en México
@app.route('/api/busiest-airport', methods=['GET'])
def get_busiest_airport():
    mycursor.execute("SELECT id_aeropuerto, COUNT(*) as movements FROM Flight GROUP BY id_aeropuerto ORDER BY movements DESC LIMIT 1")
    result = mycursor.fetchone()
    airport_id = result['id_aeropuerto']
    
    mycursor.execute("SELECT nombre_aeropuerto FROM Airport WHERE id_aeropuerto = %s", (airport_id,))
    airport_name = mycursor.fetchone()['nombre_aeropuerto']

    return jsonify({'busiest_airport': airport_name, 'movements': result['movements']})

@app.route('/api/busiest-airline', methods=['GET'])
def get_busiest_airline():
    mycursor.execute("SELECT id_aerolinea, COUNT(*) as flights_count FROM Flight GROUP BY id_aerolinea ORDER BY flights_count DESC LIMIT 1")
    result = mycursor.fetchone()
    airline_id = result['id_aerolinea']
    
    mycursor.execute("SELECT nombre_aerolinea FROM Airline WHERE id_aerolinea = %s", (airline_id,))
    airline_name = mycursor.fetchone()['nombre_aerolinea']

    return jsonify({'busiest_airline': airline_name, 'flights_count': result['flights_count']})

@app.route('/api/busiest-day', methods=['GET'])
def get_busiest_day():
    mycursor.execute("SELECT dia, COUNT(*) as flights_count FROM Flight GROUP BY dia ORDER BY flights_count DESC LIMIT 1")
    result = mycursor.fetchone()

    return jsonify({'busiest_day': result['dia'].isoformat(), 'flights_count': result['flights_count']})

@app.route('/api/aerolineas-mas-de-dos-vuelos', methods=['GET'])
def get_aerolineas_mas_de_dos_vuelos():
    mycursor.execute("SELECT id_aerolinea, COUNT(*) as flights_count FROM Flight GROUP BY id_aerolinea HAVING flights_count > 2")
    results = mycursor.fetchall()
    
    aerolineas_names = []
    for result in results:
        mycursor.execute("SELECT nombre_aerolinea FROM Airline WHERE id_aerolinea = %s", (result['id_aerolinea'],))
        aerolinea_name = mycursor.fetchone()['nombre_aerolinea']
        aerolineas_names.append(aerolinea_name)

    return jsonify({'aerolineas': aerolineas_names})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
