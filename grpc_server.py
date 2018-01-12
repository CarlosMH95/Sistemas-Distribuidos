#import sys
#import os
#sys.path.append(os.path.join(os.path.dirname(__file__), 'microservice'))
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'microservice.settings')

#from django.conf.urls import include, url
#from django.conf.urls.static import static
#from django.conf import settings
#from api.views import home, justdatabase, sendNews
import grpc
from concurrent import futures
import time
import requests
import json
import microservice_pb2
import microservice_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Microservice(microservice_pb2_grpc.MicroserviceServicer):
    def ListNews(self, request, context):
        data = requests.get('http://127.0.0.1:8000/').json()
        #data = json.loads(sedata)
        for news in data:
            yield microservice_pb2.News(id=news['pk'],title=news['fields']['title'],
                                        url=news['fields']['url'],publisher=news['fields']['publisher'],
                                        category=news['fields']['category'],story=news['fields']['story'],
                                        hostname=news['fields']['hostname'],time_stamp=news['fields']['time_stamp'],
                                        numero_accessos=news['fields']['numero_accessos'])


def serve():
    server =grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    microservice_pb2_grpc.add_MicroserviceServicer_to_server(Microservice(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
