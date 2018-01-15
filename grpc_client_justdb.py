from __future__ import print_function
import requests
import grpc

import microservice_pb2
import microservice_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = microservice_pb2_grpc.MicroserviceStub(channel)
    for news in stub.ListNews(microservice_pb2.Numero(numero=10)):
        print(news.id)


if __name__ == '__main__':
    run()
