import pytest
from trivia import Question, Quiz

def test_question_correct_answer():
	question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
	assert question.is_correct("4") # nosec

def test_question_incorrect_answer():
	question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
	assert not question.is_correct("2") # nosec

@pytest.mark.asyncio	
async def test_quiz_scoring():
	quiz=Quiz()
	question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
	quiz.add_question(question)
	await quiz.answer_question(question, "4")
	assert quiz.correct_answers == 1 # nosec

