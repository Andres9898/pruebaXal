from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Airline(db.Model):
    id_aerolinea = db.Column(db.Integer, primary_key=True)
    nombre_aerolinea = db.Column(db.String(50), nullable=False)

class Airport(db.Model):
    id_aeropuerto = db.Column(db.Integer, primary_key=True)
    nombre_aeropuerto = db.Column(db.String(50), nullable=False)

class Movement(db.Model):
    id_movimiento = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(50), nullable=False)

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_aerolinea = db.Column(db.Integer, db.ForeignKey('airline.id_aerolinea'), nullable=False)
    id_aeropuerto = db.Column(db.Integer, db.ForeignKey('airport.id_aeropuerto'), nullable=False)
    id_movimiento = db.Column(db.Integer, db.ForeignKey('movement.id_movimiento'), nullable=False)
    dia = db.Column(db.Date, nullable=False)

    airline = db.relationship('Airline', backref=db.backref('flights', lazy=True))
    airport = db.relationship('Airport', backref=db.backref('flights', lazy=True))
    movement = db.relationship('Movement', backref=db.backref('flights', lazy=True))
