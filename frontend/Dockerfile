# Establecer la imagen base
FROM node:20.15-alpine3.19

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar package.json y el archivo de la aplicación
COPY package.json /app/

# Instalar las dependencias
RUN npm install

COPY . /app/

# Construir la aplicación
RUN npm run build

# Exponer el puerto de la aplicación
EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/ || exit 1

# Comando para iniciar la aplicación
CMD ["npm", "start"]
