from flask import Flask, jsonify
import mysql.connector
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Conexión a la base de datos MySQL, cambiar por variables de entorno para mayor seguridad
mydb = mysql.connector.connect(
    host="172.18.0.5",
    user="root",
    password="password",
    database="test"
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

    return jsonify({'respondidas': answered, 'no_respondidas': unanswered})

@app.route('/api/highest-reputation', methods=['GET'])
def get_highest_reputation():
    response = requests.get('https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow')
    data = response.json()

    reputacion_mas_alta = max(data['items'], key=lambda item: item['owner']['reputation'])

    return jsonify(reputacion_mas_alta)

@app.route('/api/lowest-views', methods=['GET'])
def get_lowest_views():
    response = requests.get('https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow')
    data = response.json()

    vistas_mas_bajas = min(data['items'], key=lambda item: item['view_count'])

    return jsonify(vistas_mas_bajas)

@app.route('/api/oldest-newest', methods=['GET'])
def get_oldest_newest():
    response = requests.get('https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow')
    data = response.json()

    mas_antigua = min(data['items'], key=lambda item: item['creation_date'])
    mas_reciente = max(data['items'], key=lambda item: item['creation_date'])

    return jsonify({'mas_antigua': mas_antigua, 'mas_reciente': mas_reciente})

# Consultas SQL para datos de vuelos en México
@app.route('/api/aeropuerto-mas-ocupado', methods=['GET'])
def get_aeropuerto_mas_ocupado():
    mycursor.execute("SELECT id_aeropuerto, COUNT(*) as movimientos FROM vuelos GROUP BY id_aeropuerto ORDER BY movimientos DESC LIMIT 1")
    result = mycursor.fetchone()
    id_aeropuerto = result['id_aeropuerto']

    mycursor.execute("SELECT nombre_aeropuerto FROM aeropuertos WHERE id_aeropuerto = %s", (id_aeropuerto,))
    nombre_aeropuerto = mycursor.fetchone()['nombre_aeropuerto']

    return jsonify({'aeropuerto_mas_ocupado': nombre_aeropuerto, 'movimientos': result['movimientos']})

@app.route('/api/aerolinea-mas-activa', methods=['GET'])
def get_aerolinea_mas_activa():
    mycursor.execute("SELECT id_aerolinea, COUNT(*) as cantidad_vuelos FROM vuelos GROUP BY id_aerolinea ORDER BY cantidad_vuelos DESC LIMIT 1")
    result = mycursor.fetchone()
    id_aerolinea = result['id_aerolinea']

    mycursor.execute("SELECT nombre_aerolinea FROM aerolineas WHERE id_aerolinea = %s", (id_aerolinea,))
    nombre_aerolinea = mycursor.fetchone()['nombre_aerolinea']

    return jsonify({'aerolinea_mas_activa': nombre_aerolinea, 'cantidad_vuelos': result['cantidad_vuelos']})

@app.route('/api/dia-mas-ocupado', methods=['GET'])
def get_dia_mas_ocupado():
    mycursor.execute("SELECT dia, COUNT(*) as cantidad_vuelos FROM vuelos GROUP BY dia ORDER BY cantidad_vuelos DESC LIMIT 1")
    result = mycursor.fetchone()

    return jsonify({'dia_mas_ocupado': result['dia'].isoformat(), 'cantidad_vuelos': result['cantidad_vuelos']})

@app.route('/api/aerolineas-mas-de-dos-vuelos', methods=['GET'])
def get_aerolineas_mas_de_dos_vuelos():
    mycursor.execute("SELECT id_aerolinea, COUNT(*) as cantidad_vuelos FROM vuelos GROUP BY id_aerolinea HAVING cantidad_vuelos > 2")
    results = mycursor.fetchall()

    nombres_aerolineas = []
    for result in results:
        mycursor.execute("SELECT nombre_aerolinea FROM aerolineas WHERE id_aerolinea = %s", (result['id_aerolinea'],))
        nombre_aerolinea = mycursor.fetchone()['nombre_aerolinea']
        nombres_aerolineas.append(nombre_aerolinea)

    return jsonify({'aerolineas': nombres_aerolineas})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
