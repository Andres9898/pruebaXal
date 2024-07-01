-- Crear la base de datos si no existe y seleccionarla
CREATE DATABASE IF NOT EXISTS test;
USE test;

-- Crear la tabla aerolineas
CREATE TABLE IF NOT EXISTS aerolineas (
    id_aerolinea INT AUTO_INCREMENT PRIMARY KEY,
    nombre_aerolinea VARCHAR(50) NOT NULL
);

-- Insertar datos en la tabla aerolineas
INSERT INTO aerolineas (id_aerolinea, nombre_aerolinea) VALUES
(1, 'Volaris'),
(2, 'Aeromar'),
(3, 'Interjet'),
(4, 'Aeromexico');

-- Crear la tabla aeropuertos
CREATE TABLE IF NOT EXISTS aeropuertos (
    id_aeropuerto INT AUTO_INCREMENT PRIMARY KEY,
    nombre_aeropuerto VARCHAR(50) NOT NULL
);

-- Insertar datos en la tabla aeropuertos
INSERT INTO aeropuertos (id_aeropuerto, nombre_aeropuerto) VALUES
(1, 'Benito Juarez'),
(2, 'Guanajuato'),
(3, 'La paz'),
(4, 'Oaxaca');

-- Crear la tabla movimientos
CREATE TABLE IF NOT EXISTS movimientos (
    id_movimiento INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(50) NOT NULL
);

-- Insertar datos en la tabla movimientos
INSERT INTO movimientos (id_movimiento, descripcion) VALUES
(1, 'Salida'),
(2, 'Llegada');

-- Crear la tabla vuelos
CREATE TABLE IF NOT EXISTS vuelos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_aerolinea INT,
    id_aeropuerto INT,
    id_movimiento INT,
    dia DATE NOT NULL,
    FOREIGN KEY (id_aerolinea) REFERENCES aerolineas(id_aerolinea),
    FOREIGN KEY (id_aeropuerto) REFERENCES aeropuertos(id_aeropuerto),
    FOREIGN KEY (id_movimiento) REFERENCES movimientos(id_movimiento)
);

-- Insertar datos en la tabla vuelos
INSERT INTO vuelos (id_aerolinea, id_aeropuerto, id_movimiento, dia) VALUES
(1, 1, 1, '2021-05-02'),
(2, 1, 1, '2021-05-02'),
(3, 2, 2, '2021-05-02'),
(4, 3, 2, '2021-05-02'),
(1, 3, 2, '2021-05-02'),
(2, 1, 1, '2021-05-02'),
(2, 3, 1, '2021-05-04'),
(3, 4, 1, '2021-05-04'),
(3, 4, 1, '2021-05-04');
