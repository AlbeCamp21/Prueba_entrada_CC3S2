FROM python:3.11

# directorio de trabajo
WORKDIR /app

# Copia requirements y lo instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo al contenedor
COPY . .

# correr aplicación con Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
