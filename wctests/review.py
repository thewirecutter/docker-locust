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
        self.client.request('get','/','header=X-Pagely-Skip-Ratelimit:W0gphagw0ctOursyosufNenIalAkfin0')

    @task(7)
    def air(self):
        self.client.request('get','/best-air-purifier/','header=X-Pagely-Skip-Ratelimit:W0gphagw0ctOursyosufNenIalAkfin0')

    @task(5)
    def robot(self):
        self.client.request('get','/best-robot-vacuum/','header=X-Pagely-Skip-Ratelimit:W0gphagw0ctOursyosufNenIalAkfin0')

    @task(3)
    def humidifier(self):
        self.client.request('get','/the-best-humidifier/','header=X-Pagely-Skip-Ratelimit:W0gphagw0ctOursyosufNenIalAkfin0')
    
    @task(3)
    def bestnchead(self):
        self.client.request('get,','/best-noise-cancelling-headphones/',
                            'header=X-Pagely-Skip-Ratelimit:W0gphagw0ctOursyosufNenIalAkfin0')

    @task(3)
    def washerdryer(self):
        self.client.request('get','/the-best-washer-and-dryer/',
                            'header=X-Pagely-Skip-Ratelimit:W0gphagw0ctOursyosufNenIalAkfin0')

    @task(2)
    def wohsc(self):
        self.client.request('get','/best-wireless-outdoor-home-security-camera/',
                            'header=X-Pagely-Skip-Ratelimit:W0gphagw0ctOursyosufNenIalAkfin0')

    @task(2)
    def soundbar(self):
        self.client.request('get','/best-soundbar/','header=X-Pagely-Skip-Ratelimit:W0gphagw0ctOursyosufNenIalAkfin0')

    @task(2)
    def slippers(self):
        self.client.request('get','/best-slippers/','header=X-Pagely-Skip-Ratelimit:W0gphagw0ctOursyosufNenIalAkfin0')

    @task(2)
    def towel(self):
        self.client.request('get','/best-bath-towel/','header=X-Pagely-Skip-Ratelimit:W0gphagw0ctOursyosufNenIalAkfin0')

    @task(2)
    def doorbell(self):
        self.client.request('get','/best-smart-doorbell-camera/',
                            'header=X-Pagely-Skip-Ratelimit:W0gphagw0ctOursyosufNenIalAkfin0')
    
    @task(2)
    def heater(self):
        self.client.request('get','/best-space-heaters/','header=X-Pagely-Skip-Ratelimit:W0gphagw0ctOursyosufNenIalAkfin0')

    @task(3)
    def earbuds(self):
        self.client.request('get','/best-wireless-earbuds/','header=X-Pagely-Skip-Ratelimit:W0gphagw0ctOursyosufNenIalAkfin0')

    @task(2)
    def exheadphones(self):
        self.client.request('get','/best-wireless-exercise-headphones/',
                            'header=X-Pagely-Skip-Ratelimit:W0gphagw0ctOursyosufNenIalAkfin0')

    @task(2)
    def carryon(self):
        self.client.request('get','/best-carry-on-luggage/','header=X-Pagely-Skip-Ratelimit:W0gphagw0ctOursyosufNenIalAkfin0')
    

    @task(6)
    def inear(self):
        self.client.request('get','/best-noise-cancelling-in-ear-headphones/',
                            'header=X-Pagely-Skip-Ratelimit:W0gphagw0ctOursyosufNenIalAkfin0')


class MyLocust(HttpLocust):
    task_set = SimpleBehavior
    min_wait = 0
    max_wait = 0
