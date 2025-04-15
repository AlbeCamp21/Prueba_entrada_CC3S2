import asyncio
from db import fetch_questions_by_difficulty

class Question:
	def __init__(self, description, options, correct_answer):
		self.description = description
		self.options = options
		self.correct_answer = str(correct_answer)

	def is_correct(self, answer):
		return self.correct_answer == answer


class Quiz:
	def __init__(self):
		self.questions = []
		self.current_question_index = 0
		self.correct_answers = 0
		self.incorrect_answers = 0
		self.difficulty = 0
		self.correct_streak = 0
		self.incorrect_streak = 0
	
	async def load_questions(self):
		self.questions = await self._fetch_questions()
		
	async def _fetch_questions(self):
		filas = await fetch_questions_by_difficulty(self.difficulty)
		return [Question(row["question"], [row["option1"], row["option2"], row["option3"], row["option4"]], row["correct_answer"]) for row in filas]
		
	async def get_next_question(self):
		if self.current_question_index >= len(self.questions):
			self.questions = await self._fetch_questions()
			self.current_question_index = 0
		question = self.questions[self.current_question_index]
		self.current_question_index += 1
		return question
		
	async def answer_question(self, question, answer):
		if question.is_correct(answer):
			print("¡Correcto! ✅")
			self.correct_answers += 1
			self.correct_streak += 1
			self.incorrect_streak = 0
			if self.correct_streak == 2 and self.difficulty < 2:
				self.difficulty += 1
				self.correct_streak = 0
				print("\n---> Subiendo de dificultad --->")
				await self.load_questions()
		else:
			print("Incorrecto ❌")
			self.incorrect_answers += 1
			self.incorrect_streak += 1
			self.correct_streak = 0
			if self.incorrect_streak == 2 and self.difficulty > 0:
				self.difficulty -= 1
				self.incorrect_streak = 0
				print("\n<--- Bajando de dificultad <---")
				await self.load_questions()
                

async def run_quiz():
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
	await quiz.load_questions()
	for i in range(10):
		print(f"\n Pregunta {i + 1} (Dificultad: {quiz.difficulty})")
		question = await quiz.get_next_question()
		print(f"{question.description}")
		for idx, opt in enumerate(question.options):
			print(f"{idx + 1}) {opt}")
		answer = input("Tu respuesta: ")
		await quiz.answer_question(question, answer)
	print("\nJuego terminado!!!")
	print(f"Respuestas correctas: {quiz.correct_answers}")
	print(f"Respuestas incorrectas: {quiz.incorrect_answers}")


if __name__ == "__main__":
	asyncio.run(run_quiz())
