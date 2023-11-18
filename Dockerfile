FROM python:3.8

# Etiqueta del mantenedor
LABEL maintainer="marcia.gutierrez@utec.edu.pe"

# Instala git
RUN apt-get update && apt-get install -y git

# Clona tu repositorio de GitHub dentro del directorio /app
RUN git clone -q https://github.com/aikram/cocktails /app

# Establece el directorio de trabajo en /app
WORKDIR /app

# Instala las dependencias especificadas en requirements.txt
RUN pip install -r requirements.txt

# Expone el puerto 8000 para que sea accesible desde fuera del contenedor
EXPOSE 7000

# Define la variable de entorno NAME como FlaskApp
ENV NAME FlaskApp

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
