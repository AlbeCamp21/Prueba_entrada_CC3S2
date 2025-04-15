from dotenv import load_dotenv, find_dotenv
import os

# Carga automáticamente el archivo .env más cercano
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

print(f"[DEBUG] dotenv_path: {dotenv_path}")
print(f"[DEBUG] DATABASE_URL: {DATABASE_URL}")
