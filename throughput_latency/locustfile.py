from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        
    #@task(2)
    #def mostrardb(self):
    #   self.client.get("/noticias/mostrar/")

    @task(1)
    def mostrar(self):
        self.client.get("/noticias/mostrardb/")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 15000
