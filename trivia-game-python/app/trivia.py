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
	quiz = Quiz()
	# preguntas de ejemplo
	quiz.add_question(Question("1+1",["A) 0","B) 1","C) 2","D) 3"],"C"))
	quiz.add_question(Question("1+2",["A) 0","B) 1","C) 2","D) 3"],"D"))
	print("¡Bienvenido al juego de trivia!")
	while quiz.current_question_index < 10:
		pregunta = quiz.get_next_question()
		if pregunta is None:
			break
		print("\n",pregunta.description)
		for opcion in pregunta.options:
			print(opcion)


if __name__ == "__main__":
	run_quiz()
