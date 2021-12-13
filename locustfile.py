from locust import HttpUser, task


class QuickstartUser(HttpUser):

    nameInquiry = {
        "CHAS": {"0": 0},
        "RM": {"0": 6.575},
        "TAX": {"0": 296.0},
        "PTRATIO": {"0": 15.3},
        "B": {"0": 396.9},
        "LSTAT": {"0": 4.98},
    }

    @task
    def test_load_of_webapp(self):
        self.client.get("https://project2-ci-and-cd.azurewebsites.net")

    @task(1)
    def post(self):
        self.client.post("predict", json=QuickstartUser.nameInquiry)
