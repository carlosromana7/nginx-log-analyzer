FROM python:3.9-slim

WORKDIR /app

# Copiar solo el archivo requirements.txt primero
COPY app/requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos de la aplicación
COPY app .

# Listar el contenido del directorio para verificar
RUN ls -la

# Mostrar el contenido de los archivos principales para verificar
RUN cat app.py
RUN cat log_analyzer.py

EXPOSE 5000

CMD ["python", "app.py"]
