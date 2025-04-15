import asyncpg
from config import DATABASE_URL

async def get_connection():
	return await asyncpg.connect(DATABASE_URL)

async def fetch_questions_by_difficulty(difficulty: int, limit: int = 10):
	conn = await get_connection()
	try:
		rows = await conn.fetch(
			"SELECT question, option1, option2, option3, option4, correct_answer FROM questions WHERE difficulty = $1 ORDER BY RANDOM() LIMIT $2",
			difficulty, limit
		)
		return rows
	finally:
		await conn.close()

