from fastapi.testclient import TestClient
import importlib.util
import sys
from pathlib import Path

main_path = Path(__file__).resolve().parents[2] / "trivia-game-python" / "app" / "main.py"

spec = importlib.util.spec_from_file_location("main", str(main_path))
main = importlib.util.module_from_spec(spec)
sys.modules["main"] = main
spec.loader.exec_module(main)

client = TestClient(main.app)

def test_create_question():
	response = client.post("/questions/", json={
		"description": "What is 2 + 2?",
		"options": ["1", "2", "3", "4"],
		"correct_answer": "4"
	})
	assert response.status_code == 201

