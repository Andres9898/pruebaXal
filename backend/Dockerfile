# Establecer la imagen base
FROM python:3.8-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar requirements.txt y el archivo de la aplicación
COPY requirements.txt requirements.txt
COPY . .

# Instalar las dependencias
RUN pip install mysql-connector-python
RUN pip install -r requirements.txt

# Exponer el puerto de la aplicación
EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/ || exit 1

# Comando para iniciar la aplicación
CMD ["python", "app.py"]
