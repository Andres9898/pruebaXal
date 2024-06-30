import mysql.connector

# Establecer la conexión con la base de datos
# Cambiar los valores por variables de entorno (no tuve tiempo de hacerlo)
db_connection = mysql.connector.connect(
    host="localhost:3306",
    user="root",
    password="password",
    database="test"
)

# Crear un cursor para ejecutar consultas
cursor = db_connection.cursor()

# Ejemplo de consulta SELECT
query = "SELECT * FROM airline"
cursor.execute(query)
airlines = cursor.fetchall()

# Iterar sobre los resultados
for airline in airlines:
    print(airline)

# Ejemplo de consulta INSERT
insert_query = "INSERT INTO airline (nombre_aerolinea) VALUES ('Jet Airways')"
cursor.execute(insert_query)
db_connection.commit()  # Confirmar la inserción

print("Datos insertados correctamente.")

# Ejemplo de consulta UPDATE
update_query = "UPDATE airline SET nombre_aerolinea = 'Nueva Aerolínea' WHERE id_aerolinea = 1"
cursor.execute(update_query)
db_connection.commit()  # Confirmar la actualización

print("Datos actualizados correctamente.")

# Ejemplo de consulta DELETE
delete_query = "DELETE FROM airline WHERE id_aerolinea = 1"
cursor.execute(delete_query)
db_connection.commit()  # Confirmar la eliminación

print("Datos eliminados correctamente.")

# Cerrar el cursor y la conexión
cursor.close()
db_connection.close()
