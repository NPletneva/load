from locust import HttpUser, between, task


class MediumUser(HttpUser):
    # how long Locust should wait before spawning additional users; new users will spawn some time every 3 to 5 seconds
    wait_time = between(3, 5)
    # the base URL
    host = 'https://medium.com/'

    # decorator is telling MediumUser class what action it needs to take when Locust is working
    @task
    def make_get_home_request(self):
        # GET request; call host API endpoint
        self.client.get(self.host, name="GET /medium homepage")
