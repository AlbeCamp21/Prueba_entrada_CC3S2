# CHANGELOG

## Día 1
1. **Commit ee56f33** (Rama feature/dia1)  
   - Archivo `requirements.txt` creado, usando `pip freeze > requirements.txt`.

2. **Commit 2742d8e** (Rama feature/dia1)  
   - Archivo `Dockerfile` creado, basándome en el código encontrado en foros como DockerHub.

3. **Commit bcd7e64** (Rama feature/dia1)  
   - Archivo `docker-compose.yml` creado, basándome nuevamente en foros como los ya mencionados.

4. **Commit 2a733e2** (Rama feature/dia1)  
   - Carpeta `app` creada, que contiene `main.py`, donde se encuentra la estructura básica para FastAPI.

5. **Commit 5cad171** (Rama develop)  
   - Merge realizado entre `feature/dia1` y `develop`.

## Día 2
1. **Commit 542cd4d** (Rama feature/dia2)  
   - Archivo `trivia.py` creado, conteniendo la clase `Question` con su constructor y función `is_correct`.

2. **Commit ab26b36** (Rama feature/dia2)  
   - Archivo `test_trivia.py` creado, archivo para hacer las pruebas unitarias del contenido de `trivia.py`.

3. **Commit bbb0ab7** (Rama develop)  
   - Merge realizado entre `feature/dia2` y `develop`.

4. **Commits 48ba677 y a365406** (Rama develop)  
   - Agregando archivos que faltaban por commitear, como `__pycache__` y `venv/`.

## Día 3
1. **Commit 2fa6922** (Rama feature/estructura-basic)  
   - Añadida la clase `Quiz`, con sus respectivas funciones, dentro del archivo `trivia.py`.

2. **Commit 39277fa** (Rama feature/estructura-basic)  
   - Añadida la función `run_quiz()` dentro del archivo `trivia.py`. Esta función imprime las preguntas de la trivia.

3. **Commit 0820fb6** (Rama develop)  
   - Merge realizado entre `feature/estructura-basic` y `develop`.
   
## Día 4
1. **Commit c6182ad** (Rama feature/dia4)  
   - Actualizada la clase `Quiz`, donde se le añade más funciones para el control de respuestas correctas e incorrectas.

2. **Commit f306aef** (Rama feature/dia4)  
   - Actualizado el archivo `test_trivia.py`, donde se le añade tests para probar el control de respuestas correctas e incorrectas.

3. **Commit aaaf78e** (Rama develop)  
   - Merge realizado entre `feature/dia4` y `develop`.
   
## Día 5
1. **Commit bb99682** (Rama feature/ui-improvements)  
   - Actualizada la función `run_quiz`, donde se le añade las 10 preguntas y se mejora relativamente la interfaz.

2. **Commit be0e9fa** (Rama feature/ui-improvements)  
   - Haciendo pruebas, se actualiza el archivo `Dockerfile` para levantar el container sin errores.

3. **Commit e263c93** (Rama feature/ui-improvements)  
   - Haciendo pruebas, se actualiza el archivo `docker-compose.yml` para levantar el container sin errores.

4. **Commit 4ac2628** (Rama feature/ui-improvements)  
   - Se mejora aún más la interfaz de usuario de `trivia.py`.
   
5. **Commit 279f423** (Rama develop)  
   - Merge realizado entre `feature/ui-improvements` y `develop`.
   
## Día 6
1. **Commit a944c96** (Rama feature/ci-cd-integration)  
   - Actualizado el archivo `docker-compose.yml`, para que cree la base de datos señalado en el archivo `init.sql`.

2. **Commit 6b201d5** (Rama feature/ci-cd-integration)  
   - Creación del archivo `init.sql` donde se crean la tabla que contendrá las preguntas clasificadas por dificultad.

3. **Commit 779812c** (Rama feature/ci-cd-integration)  
   - Directorio `.github` creado donde se encuentra `ci.yml` para la implementación de pruebas.

4. **Commit 3c57f25** (Rama feature/ci-cd-integration)  
   - Se crea el archivo `.secrets`, donde se encuentra el `SONAR_TOKEN`.
   
5. **Commit fd50eb1** (Rama feature/ci-cd-integration)  
   - Se crea el directorio `test_api`, donde se encuentra el archivo `test_api.py` para pruebas con fastapi.

6. **Commit a39bf16** (Rama feature/ci-cd-integration)  
   - Directorio `routes` creado como convención de fastapi para mejorar la organización del código .

7. **Commit d5d669d** (Rama feature/ci-cd-integration)  
   - `main.py` actualizado para que trabaje con el directorio `routes`.
   
8. **Commit dc009cf** (Rama develop)  
   - Merge realizado entre `feature/ci-cd-integration` y `develop`.

