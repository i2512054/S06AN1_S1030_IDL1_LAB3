from locust import HttpUser, SequentialTaskSet, task, between
class SerialBehavior(SequentialTaskSet):
	@task
	def fetch_posts_list(self):
		self.client.get("/posts", name="1_GET_/posts_Serial")
	
	@task
	def fetch_single_post(self):
		self.client.get("/posts/1", name="2_GET_/posts/1_Serial")
		
class IntermediateSerialUser(HttpUser):
	host = "https://jsonplaceholder.typicode.com"
	wait_time = between(1, 3)
	tasks = [SerialBehavior]