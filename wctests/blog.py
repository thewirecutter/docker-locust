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

    @task(5)
    def bike(self):
        self.client.get('/when-to-replace-your-bike-helmet/')

    @task(2)
    def online(self):
        self.client.get('/online-therapy-experience/')

    @task(6)
    def keyboard(self):
        self.client.get('/why-i-love-compact-mechanical-keyboards-and-you-will-too/')
    
    @task(5)
    def modem(self):
        self.client.get('/modem-vs-router/')

    @task(8)
    def sofa(self):
        self.client.get('/sofa-buying-advice/')

    @task(4)
    def apple(self):
        self.client.get('/all-the-new-apple-stuff-october-2014/')

    @task(2)
    def nyt(self):
        self.client.get('/the-new-york-times-has-acquired-the-wirecutter/')
    
    @task(5)
    def bosch(self):
        self.client.get('/is-bosch-a-reliable-brand-for-kitchen-appliances/')

    @task(3)
    def therapy(self):
        self.client.get('/text-therapy/')


class MyLocust(HttpLocust):
    task_set = SimpleBehavior
    min_wait = 0
    max_wait = 0
