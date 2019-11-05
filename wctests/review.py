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
        self.client.get('/')

    @task(7)
    def air(self):
        self.client.get('/best-air-purifier/')

    @task(5)
    def robot(self):
        self.client.get('/best-robot-vacuum/')

    @task(3)
    def humidifier(self):
        self.client.get('/the-best-humidifier/')
    
    @task(3)
    def bestnchead(self):
        self.client.get('/best-noise-cancelling-headphones/')

    @task(3)
    def washerdryer(self):
        self.client.get('/the-best-washer-and-dryer/')

    @task(2)
    def wohsc(self):
        self.client.get('/best-wireless-outdoor-home-security-camera/')

    @task(2)
    def soundbar(self):
        self.client.get('/best-soundbar/')

    @task(2)
    def slippers(self):
        self.client.get('/best-slippers/')

    @task(2)
    def towel(self):
        self.client.get('/best-bath-towel/')

    @task(2)
    def doorbell(self):
        self.client.get('/best-smart-doorbell-camera/')
    
    @task(2)
    def heater(self):
        self.client.get('/best-space-heaters/')

    @task(3)
    def earbuds(self):
        self.client.get('/best-wireless-earbuds/')

    @task(2)
    def exheadphones(self):
        self.client.get('/best-wireless-exercise-headphones/')

    @task(2)
    def carryon(self):
        self.client.get('/best-carry-on-luggage/')
    

    @task(6)
    def inear(self):
        self.client.get('/best-noise-cancelling-in-ear-headphones/')


class MyLocust(HttpLocust):
    task_set = SimpleBehavior
    min_wait = 0
    max_wait = 0
