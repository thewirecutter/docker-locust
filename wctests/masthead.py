from locust import HttpLocust
from locust import TaskSet
from locust import task
from locust.web import app

from src import report

# For reporting
app.add_url_rule('/htmlreport', 'htmlreport', report.download_report)


class SimpleBehavior(TaskSet):

    @task(1)
    def index(self):
        self.client.request('get', '/masthead/', 'header=X-Pagely-Skip-Ratelimit:W0gphagw0ctOursyosufNenIalAkfin0')


class MyLocust(HttpLocust):
    task_set = SimpleBehavior
    min_wait = 0
    max_wait = 0
