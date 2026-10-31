from locust import HttpUser, task, between

class AdvancedPayloadUser(HttpUser):
    host = "https://jsonplaceholder.typicode.com"
    wait_time = between(0.5, 1.5)

    @task(2)
    def send_basic_payload(self):
        payload = {'userId': 1, 'title': 'Basic Payload Test', 'body': 'Short Content body text'}
        self.client.post("/posts", json=payload, name="POST_/posts_Basic")

    @task(1)
    def send_heavy_payload(self):
        heavy_text = "X" * 50000 # Payload pasado de ~50 KB
        payload = {
            "userId": 1,
            "title": "Heavy Payload Stress Test",
            "body": heavy_text,
            "metadata": { "data": "A" * 10000 }
        }
        self.client.post("/posts", json=payload, name="POST_/posts_Heavy")
