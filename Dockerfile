# Usar una imagen ligera de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código fuente
COPY . .

# Comando por defecto al ejecutar el contenedor 
# (Ajusta "main.py" si tu archivo principal se llama diferente)
CMD ["python", "main.py"]