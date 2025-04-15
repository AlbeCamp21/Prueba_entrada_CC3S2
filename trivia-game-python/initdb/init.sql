-- initdb/init.sql

-- Creación de la tabla questions
CREATE TABLE IF NOT EXISTS questions (
	id SERIAL PRIMARY KEY,
	question TEXT NOT NULL,
	option1 TEXT NOT NULL,
	option2 TEXT NOT NULL,
	option3 TEXT NOT NULL,
	option4 TEXT NOT NULL,
	correct_answer INTEGER NOT NULL CHECK (correct_answer BETWEEN 1 AND 4),
	difficulty SMALLINT NOT NULL CHECK (difficulty BETWEEN 0 AND 2)
);


-- Dificultad fácil
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿Cuál es la capital de Francia?', 'Madrid', 'Berlín', 'París', 'Roma', 3, 0);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿En qué continente se encuentra Egipto?', 'Asia', 'Europa', 'África', 'América', 3, 0);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿Cuál es el elemento químico con el símbolo "O"?', 'Oro', 'Oxígeno', 'Osmio', 'Oxalato', 2, 0);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿Qué planeta es conocido como el planeta rojo?', 'Marte', 'Júpiter', 'Saturno', 'Venus', 1, 0);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿Cuál es el océano más grande del mundo?', 'Atlántico', 'Índico', 'Ártico', 'Pacífico', 4, 0);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿Qué animal es conocido por su gran tamaño?', 'Elefante', 'Ratón', 'Gato', 'Conejo', 1, 0);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿Cuál es el color del cielo en un día despejado?', 'Verde', 'Azul', 'Rojo', 'Amarillo', 2, 0);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿Cuántos días tiene una semana?', '5', '6', '8', '7', 4, 0);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿Qué bebida se obtiene de la fermentación de la uva?', 'Cerveza', 'Vino', 'Whisky', 'Ron', 2, 0);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿Cuál es el primer mes del año en el calendario gregoriano?', 'Marzo', 'Enero', 'Febrero', 'Diciembre', 2, 0);

-- Dificultad media
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿Quién escribió "Cien años de soledad"?', 'Pablo Neruda', 'Gabriel García Márquez', 'Julio Cortázar', 'Mario Vargas Llosa', 2, 1);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿Qué instrumento se utiliza para medir la intensidad de los terremotos?', 'Termómetro', 'Sismógrafo', 'Barómetro', 'Anemómetro', 2, 1);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿Quién pintó la Mona Lisa?', 'Leonardo da Vinci', 'Miguel Ángel', 'Van Gogh', 'Picasso', 1, 1);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿Qué instrumento se utiliza para medir la temperatura?', 'Barómetro', 'Termómetro', 'Higrómetro', 'Anemómetro', 2, 1);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿Quién escribió "La Odisea"?', 'Sófocles', 'Aristófanes', 'Eurípides', 'Homero', 4, 1);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿Cuál es el río más largo del mundo?', 'Nilo', 'Yangtsé', 'Amazonas', 'Misisipi', 3, 1);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿En qué país se originó el tango?', 'Brasil', 'Chile', 'Uruguay', 'Argentina', 4, 1);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿Qué gas es necesario para la respiración humana?', 'Oxígeno', 'Dióxido de carbono', 'Helio', 'Nitrógeno', 1, 1);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿Cuál es el nombre del proceso por el que las plantas producen su alimento?', 'Respiración', 'Digestión', 'Fotosíntesis', 'Transpiración', 3, 1);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿Qué país tiene forma de bota?', 'España', 'Portugal', 'Grecia', 'Italia', 4, 1);


-- Dificultad difícil
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿Cuál es el idioma más hablado en el mundo?', 'Inglés', 'Hindi', 'Español', 'Chino mandarín', 4, 2);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿En qué año llegó el hombre a la Luna?', '1965', '1969', '1971', '1975', 2, 2);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿Cuál fue la causa principal de la caída del Imperio Romano de Occidente?', 'Invasiones bárbaras', 'Crisis económica', 'Problemas políticos internos', 'Todas las anteriores', 4, 2);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿Qué filósofo griego es conocido por la frase "Solo sé que no sé nada"?', 'Platón', 'Sócrates', 'Aristóteles', 'Heráclito', 2, 2);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿Cuál es la obra literaria considerada la primera novela moderna?', 'El Quijote', 'Don Juan Tenorio', 'La Celestina', 'La Regenta', 1, 2);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿Qué descubrimiento revolucionó la ciencia en el siglo XIX al posibilitar el estudio de las células?', 'La imprenta', 'La fotografía', 'El microscopio', 'La célula', 3, 2);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿En qué año se firmó la Declaración de Independencia de los Estados Unidos?', '1776', '1783', '1801', '1812', 1, 2);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿Cuál es la teoría que explica el origen del universo mediante una expansión a partir de un estado extremadamente denso y caliente?', 'Teoría del Estado Estacionario', 'Teoría M', 'Teoría del Big Bang', 'Teoría de la Relatividad', 3, 2);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿Qué descubrimiento permitió conectar los continentes mediante un puente terrestre hace millones de años?', 'El Istmo de Panamá', 'El Puente Beringiano', 'El Desierto de Gobi', 'El Mar Mediterráneo', 2, 2);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer, difficulty) VALUES ('¿Qué científico es reconocido por la formulación de las leyes del movimiento y la gravitación universal?', 'Albert Einstein', 'Isaac Newton', 'Galileo Galilei', 'Nikola Tesla', 2, 2);


