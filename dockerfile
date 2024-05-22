# Utilizar la versión más reciente de Alpine Linux como imagen base
FROM alpine:latest

# Instalar Python 3, pip y otras dependencias necesarias
RUN apk add --no-cache python3 py3-pip bash

# Crear un directorio de la aplicación en el contenedor
RUN mkdir -p /usr/src/app

# Copiar requirements.txt al directorio de la aplicación
COPY requirements.txt /usr/src/app/

# Crear y activar un entorno virtual, luego instalar las dependencias de Python
RUN python3 -m venv /usr/src/app/venv
RUN /usr/src/app/venv/bin/pip install --upgrade pip
RUN /usr/src/app/venv/bin/pip install --no-cache-dir -r /usr/src/app/requirements.txt

# Copiar el código de la aplicación y la plantilla HTML al contenedor
COPY app.py /usr/src/app/
COPY templates /usr/src/app/templates
COPY static /usr/src/app/static

# Exponer el puerto 5000 para acceder a la aplicación Flask
EXPOSE 5000

# Comando para ejecutar la aplicación Flask dentro del entorno virtual
CMD ["/bin/bash", "-c", ". /usr/src/app/venv/bin/activate && python /usr/src/app/app.py"]
