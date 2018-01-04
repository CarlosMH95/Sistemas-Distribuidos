# Sistemas Distribuidos
○ Web frontend: 2 puntos<br>
○ Microservicio con uso correcto de RPC con formato binario: 6 puntos   <br>  
○ Acceso correcto a BD: 2 puntos <br>
○ Acceso correcto a Caché, incluyendo inserciones en la caché, cuando no se
encuentra lo que se busca: 6 puntos<br>
○ Se ha incluido un Makefile que permite compilar el proyecto en la línea de
comando + README que explique lo necesario para compilar/instalar el SW: 1
punto<br>
○ Deployment en la nube: 5 puntos.<br>
○ Pruebas de rendimiento correctamente realizadas y correctamente
documentadas (incluye el uso de una herramienta de benchmarking, o la
implementación de scripts de prueba): 6 puntos<br>
○ EXTRAS: Hasta 5 puntos, dependiendo de lo implementado.<br>
<br>
Microservicio + Memcached
<br>
El DUMP de la database es gigante y no puedo pasarlo :'v <br>
Para que funcione el microservicio de django se necesitan las siguientes dependencias. (Obviamente también instalado memcached)<br>
python 3+<br>
django-corsheaders (no me acuerdo si está bien escrito...)<br>
django-memcached<br>
python-memcached<br>
<br>
NO OLVIDAR CAMBIAR EL PASSWORD DE LA DATABASE EN SETTINGS.PY<br>
La base de datos que creen debe llamarse newsfeed<br>
<br>
URLS<br>
database + cache: localhost:8000<br>
<br>
only database: localhost:8000/justdatabase<br>
<br>
gRPC PRE REQUISITOS<br>
gRPC Python is supported for use with Python 2.7 or Python 3.4 or higher<br>
$ python -m pip install --upgrade pip<br>
$ python -m pip install grpcio<br>
$ python -m pip install grpcio-tools<br>
<br>
From the examples/helloworld directory:
1. Run the server<br>
$ python greeter_server.py<br>
2. In another terminal, run the client<br>
$ python greeter_client.py<br>
<br>
Si encuentran algún error, informar
