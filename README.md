# SISTEMAS DISTRIBUIDOS
<strong>IMPLEMENTACIÓN</strong>
<br>
○ Web frontend: 2 puntos.<br>
○ Microservicio con uso correcto de RPC con formato binario: 6 puntos.  
○ Acceso correcto a BD: 2 puntos.<br>
○ Acceso correcto a Caché, incluyendo inserciones en la caché, cuando no se
encuentra lo que se busca: 6 puntos.<br>
○ Se ha incluido un Makefile que permite compilar el proyecto en la línea de
comando + README que explique lo necesario para compilar/instalar el SW: 1
punto.<br>
○ Deployment en la nube: 5 puntos.<br>
○ Pruebas de rendimiento correctamente realizadas y correctamente
documentadas (incluye el uso de una herramienta de benchmarking, o la
implementación de scripts de prueba): 6 puntos.<br>
○ EXTRAS: Hasta 5 puntos, dependiendo de lo implementado.<br>
<br>
<strong>DEPENDENCIAS</strong>
<br>
○ django==2.0<br>
○ django-bootstrap-themes==3.3.6<br>
○ django-bootstrap3==9.1.0<br>
○ django-cors-headers==2.1.0<br>
○ django-memcached==0.1.2<br>
○ django-uwsgi==0.2.1<br>
○ grpcio==1.8.3<br>
○ grpcio-tools==1.8.3<br>
○ mysqlclient==1.3.12<br>
○ protobuf==3.5.1<br>
○ PyMySQL==0.8.0<br>
○ pyparsing==2.2.0<br>
○ python-dateutil==2.6.1<br>
○ python-memcached==1.59<br>
○ requests==2.18.4<br>
<br>
<strong>USO</strong>
<br>
Iniciar los 3 servidores (archivos de python):<br>
○ grpc_server.py (microservicio base datos + cache)<br>
○ grpc_server_justdb.py (microservicio solo base de datos<br>
○ gprc_gateway.py (api gateway / reverse proxy)<br>
<br>
En el navegador entrar a la dirección localhost:9000 para ir al microservicio con cache<br>
Si quiere solo probar base de datos, ir a localhost:9000/justdb<br>
<br>
<strong>AMAZON WEB SERVICE</strong>
<br>
○ Ingresar desde AWS console https://648683556505.signin.aws.amazon.com/console<br>
○ Credenciales de autenticación<br>
○ Buscar el servicio <strong>EC2</strong><br>
○ Seleccionar la opción <strong>instancias</strong><br>
<br>
<strong>CONECTARSE VIA PUTTY</strong>
<br>
○ Abrir PUTTY<br>
○ En hostname colocar Public DNS (IPv4) que corresponda a la instancia que desea conectar.<br>
○ Buscar la sección Data y ponen <strong>ubuntu</strong> el campo Auto-login user name.<br>
○ Luego se van a la sección SSH submenú Auth y cargan el django-key.ppk desde el el explorador de archivos.<br>
○ Finalmente dan clic en open.<br>
<br>
<strong>ANTES DE COMENZAR</strong>
<br>
○ Ejecutar el virtualenv (No tienen que instalar nada solo ejecutar comandos de abajo).<br>
_$ virtualenv -p python3 /tmp/djangodev<br>
_$ . /tmp/djangodev/bin/activate<br>
○ Usar el comando <strong>deactivate</strong> en caso que deseen salir del virtualenv<br>
<br>
<strong>INSTANCIAS CONFIGURADAS</strong>
<br>
○ django-webapp (aplicación web)<br>
○ django-gateway (reverse proxy)<br>
○ django-microservice (microservicio db)<br>
○ django-memcached (microservicio con memcached)<br>
○ django-db (base de datos)<br>
<br>
<strong>DJANGO WEBAPP</strong>
<br>
○ Ubicarse en el directorio webapp<br>
○ python manage.py runserver 172.31.34.84:8000<br>
<br>
<strong>CONFIGURACIÓN DE LAS INSTANCIAS</strong>
<br>
_$ sudo apt-get update<br>
_$ sudo apt-get install virtualenv<br>
_$ virtualenv -p python3 /tmp/djangodev<br>
_$ . /tmp/djangodev/bin/activate<br>
_$ pip install django<br>
_$ pip install django-memcached<br>
_$ pip install django-cors-headers<br>
_$ pip install django-bootstrap-themes<br>
_$ pip install requests<br>
_$ pip install grpcio<br>
_$ pip install grpcio-tools<br>
_$ pip install protobuf<br>
_$ pip install python-memcached<br>
_$ deactivate<br>
_$ sudo apt-get install mysql-server<br>
_$ sudo apt-get install libmysqlclient-dev<br>
_$ sudo apt-get install python3-pip<br>
_$ sudo pip3 install mysqlclient<br>
_$ . /tmp/djangodev/bin/activate<br>
_$ pip install pymysql<br>
_$ pip install mysqlclient<br>
_$ pip install awscli<br>
_$ aws configure<br>
_$ Access key ID: *********************<br>
_$ Secret access key: ************************<br>
_$ us-west-2<br>
_$ json<br>
_$ git --version<br>
_$ git clone (repository)<br>


