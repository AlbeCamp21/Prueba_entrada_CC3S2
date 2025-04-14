class Question:
	def __init__(self, description, options, correct_answer):
		self.description = description
		self.options = options
		self.correct_answer = correct_answer

	def is_correct(self, answer):
		return self.correct_answer == answer


class Quiz:
	def __init__(self):
		self.questions = []
		self.current_question_index = 0
		self.correct_answers = 0
		self.incorrect_answers = 0

	def add_question(self, question):
		self.questions.append(question)

	def get_next_question(self):
		if self.current_question_index < len(self.questions):
			question = self.questions[self.current_question_index]
			self.current_question_index += 1
			return question
		return None
		
	def answer_question(self, question, answer):
		if question.is_correct(answer):
			self.correct_answers += 1
			return True
		else:
			self.incorrect_answers += 1
			return False

def run_quiz():
	print(r"""
 _____    _       _         _____                      
|_   _|  (_)     (_)       |  __ \                     
  | |_ __ ___   ___  __ _  | |  \/ __ _ _ __ ___   ___ 
  | | '__| \ \ / / |/ _` | | | __ / _` | '_ ` _ \ / _ \
  | | |  | |\ V /| | (_| | | |_\ \ (_| | | | | | |  __/
  \_/_|  |_| \_/ |_|\__,_|  \____/\__,_|_| |_| |_|\___|

         __  
 ___  ___\ \ 
(___)(___)> >  Responde las siguientes preguntas seleccionando el número de la opción correcta!!!
         /_/ 


                                                  
""")
	quiz = Quiz()
	# preguntas de ejemplo
	quiz.add_question(Question("¿Cuál es la capital de Francia?", ["Madrid", "Berlín", "París", "Roma"], "3"))
	quiz.add_question(Question("¿Quién escribió 'Cien años de soledad'?", ["Pablo Neruda", "Gabriel García Márquez", "Julio Cortázar", "Mario Vargas Llosa"], "2"))
	quiz.add_question(Question("¿En qué continente se encuentra Egipto?", ["Asia", "Europa", "África", "América"], "3"))
	quiz.add_question(Question("¿Cuál es el elemento químico con el símbolo 'O'?", ["Oro", "Oxígeno", "Osmio", "Oxalato"], "2"))
	quiz.add_question(Question("¿Qué planeta es conocido como el planeta rojo?", ["Marte", "Júpiter", "Saturno", "Venus"], "1"))
	quiz.add_question(Question("¿En qué año llegó el hombre a la Luna?", ["1965", "1969", "1971", "1975"], "2"))
	quiz.add_question(Question("¿Cuál es el océano más grande del mundo?", ["Atlántico", "Índico", "Ártico", "Pacífico"], "4"))
	quiz.add_question(Question("¿Quién pintó la Mona Lisa?", ["Leonardo da Vinci", "Miguel Ángel", "Van Gogh", "Picasso"], "1"))
	quiz.add_question(Question("¿Qué instrumento mide la intensidad de los terremotos?", ["Termómetro", "Sismógrafo", "Barómetro", "Anemómetro"], "2"))
	quiz.add_question(Question("¿Cuál es el idioma más hablado en el mundo?", ["Inglés", "Hindi", "Español", "Chino mandarín"], "4"))

	while quiz.current_question_index < 10:
		question = quiz.get_next_question()
		if question:
			print(f"\nPregunta {quiz.current_question_index}: {question.description}")
			for idx, option in enumerate(question.options):
				print(f"{idx + 1}) {option}")
			answer = input("Tu respuesta: ")
			if quiz.answer_question(question, answer):
				print("¡Correcto! ✅")
			else:
				print("Incorrecto ❌")
		else:
			break
	print("\nJuego terminado!!!")
	print(f"\nPreguntas contestadas: {quiz.current_question_index}")
	print(f"Respuestas correctas: {quiz.correct_answers}")
	print(f"Respuestas incorrectas: {quiz.incorrect_answers}")


if __name__ == "__main__":
	run_quiz()
