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
<br>
DEPENDENCIAS:<br>
Es necesario instalar las siguientes dependencias:<br>
-Python 3.6.1 o superior.<br>
-gRPC para Python, eso incluye: <br>
---$ python -m pip install --upgrade pip<br>
---$ python -m pip install grpcio<br>
---$ python -m pip install grpcio-tools<br>
-Memcached (1.4.5 fue el que yo usé en Windows)<br>
-Conector de Python con Memcached, esto es: <br>
---$ python -m pip install python-memcached<br>
-Conector de Python con MySQL sencillo, este:<br>
---$ python -m pip install PyMySQL<br>
<br>
(No me acuerdo de las otras dependencias, si notas que falta algo Manosalvas ponlo :v)
<br>
<br>
USO:<br><br>
Iniciar los 3 servidores (archivos de python):<br>
-grpc_server.py (microservicio base datos + cache)<br>
-grpc_server_justdb.py (microservicio solo base de datos<br>
-gprc_gateway.py (api gateway / reverse proxy)<br>
<br>
En el navegador entrar a la dirección localhost:9000 para ir al microservicio con cache<br>
Si quiere solo probar  base de datos, ir a localhost:9000/justdb
AMAZON WEB SERVICE:<br>
○ Ingresar desde AWS console https://648683556505.signin.aws.amazon.com/console
○ Credenciales de autenticación fuerón enviadas a sus emails.<br>
○ En la barra de búsqueda buscar el servicio EC2<br>
○ En el menú lateral izquierdo clic en la opción instancias<br>
CONECTARSE VIA PUTTY<br>
○ Abrir PUTTY
○ En hostname poner la Public DNS (IPv4) que corresponda a la instancia a la que se quieren conectar.
○ Buscan la seccion Data en PUTTY y ponen "ubuntu" el campo Auto-login user name
○ Luego se van a la sección SSH submenú Auth y cargan el django-key.ppk desde el el explorador de archivos.
○ Finalmente dan clic en open.
ANTES DE COMENZAR<br>
○ Ejecutar el virtualenv (No tienen que instalar nada solo ejecutar comandos de abajo).
○ virtualenv -p python3 /tmp/djangodev
○ . /tmp/djangodev/bin/activate
○ Usar el comando deactivate en caso que deseen salir del virtualenv
EN LA INSTANCIA WEBAPP<br>
○ Ubicarse en el directorio webapp
○ python manage.py runserver 172.31.34.84:8000
SOBRE LAS INSTANCIAS<br>
○ django-webapp <aplicación web>
○ django-gateway <reverse proxy>
○ django-microservice <microservicio db>
○ django-memcached <microservicio con memcached>
○ django-db <base de datos>




