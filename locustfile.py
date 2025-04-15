from locust import HttpUser, task

class TriviaUser(HttpUser):
	@task
	def get_home(self):
		self.client.get("/")
    
	@task
	def post_question(self):
		self.client.post("/questions/", json={
			"description": "¿Cuál es la capital de Francia?",
			"options": ["Madrid", "Berlín", "París", "Lisboa"],
			"correct_answer": "París"
		})

