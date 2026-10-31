from locust import HttpUser, task, between
class ParallelUser(HttpUser):
	host = "https://jsonplaceholder.typicode.com"
	wait_time = between(1, 2)
	
	@task(3)
	def fetch_posts_list(self):
		self.client.get("/posts", name="GET_/posts_Parallel")
		
	@task(1)
	def fetch_single_post(self):
		self.client.get("/posts/1", name="GET_/posts/1_Parallel")