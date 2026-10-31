from locust import HttpUser, task, between
class BasicUser(HttpUser):
	host = ""
	wait_time = between(1,2)
	
	@task
	def get_all_posts(self):
		with self.client.get("/posts", catch_response=True) as response:
			if response.status_code == 200:
				response.success()
			else:
				response.failure(f"Error {response.status_code}")