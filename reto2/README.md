# info de la materia: ST0263
#
# Estudiante(s): Daniel Arango Hoyos, darangoh@eafit.edu.co
#
# Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#
# Implementación Middleware: RPC y MoM
#
# 1. breve descripción de la actividad
#
La finalidad de este reto es la de implementar dos middlewares, uno RPC y otro MoM, los cuales, a través de un API Gateway, proveerán dos microservicios bastante sencillos a los consumidores.
## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
-Se implementaron los middlewares RPC y MoM.
-Se logró comunicar a los microservicios desde una API gateway a través de estos Middlewares.
-Se implementaron scripts para la instalación de dependencias y otro para la ejecución del proyecto.
-Se desarrolló cierto grado de tolerancia a errores en el microservicio de búsquedas.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
-Balanceador de cargas o roundrobin.
-Que el proyecto se ejecute cuando se inicie la máquina.

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

![image](https://user-images.githubusercontent.com/61467004/223319533-e2f1eaf3-3ffe-4dbb-93d4-90c0e92f1ce0.png)

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

## como se compila y ejecuta.

-Se abre el puerto 5000 en las reglas de seguridad de AWS.
-Se realiza un git clone https://github.com/Drealm-bot/darangoh-st0263
-Se dirige hacia el directorio darangoh-st0263 (cd darangoh-st0263/)
-Se ejecuta el script de install.sh (sudo bash install.sh)
-Se ejecuta el script de run.sh (sudo bash run.sh)
-Se dirige hacia la IP-publica:5000
-Se comprueba los archivos disponibles (IP-publica:5000/files)
-Se buscan los archivos deseados (IP-publica:5000/search?query=nombredelarchivo)

## detalles del desarrollo.

Se corre en ubuntu.

## detalles técnicos

- Ubuntu 22.04
- python 3.10.6.
- Flask 2.2.3
- grpcio 1.51.3
- grpc-tools 1.51.3
- pika 1.3.1

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)

Se tiene que abrir el puerto 5000 dentro de los grupos de seguridad de AWS para que el usuario se pueda comunicar con la API Gateway.

## opcional - detalles de la organización del código por carpetas o descripción de algún archivo. (ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO, comando 'tree' de linux)

![image](https://user-images.githubusercontent.com/61467004/223318295-7fd6322c-45e6-4c5c-9b47-dd229a04b44a.png)

## 
## opcionalmente - si quiere mostrar resultados o pantallazos 

![image](https://user-images.githubusercontent.com/61467004/223318432-4ae5a474-cb3b-4aad-8c8b-29ef118b2cb7.png)
![image](https://user-images.githubusercontent.com/61467004/223318645-419b89ff-8a56-4656-83ea-add30866eda9.png)
![image](https://user-images.githubusercontent.com/61467004/223318692-5dc4a99d-8ce6-439f-8596-f2a432ddd3af.png)

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

- python 3.10.6.
- Flask 2.2.3
- grpcio 1.51.3
- grpc-tools 1.51.3
- pika 1.3.1

# IP o nombres de dominio en nube o en la máquina servidor.

La IP es la IP pública de la instancia EC2.

## una mini guia de como un usuario utilizaría el software o la aplicación

-Se abre el puerto 5000 en las reglas de seguridad de AWS.
-Se realiza un git clone https://github.com/Drealm-bot/darangoh-st0263
-Se dirige hacia el directorio darangoh-st0263 (cd darangoh-st0263/)
-Se ejecuta el script de install.sh (sudo bash install.sh)
-Se ejecuta el script de run.sh (sudo bash run.sh)
-Se dirige hacia la IP-publica:5000
-Se comprueba los archivos disponibles (IP-publica:5000/files)
-Se buscan los archivos deseados (IP-publica:5000/search?query=nombredelarchivo)

# 5. otra información que considere relevante para esta actividad.

Eso es todo.

# referencias:
<debemos siempre reconocer los créditos de partes del código que reutilizaremos, así como referencias a youtube, o referencias bibliográficas utilizadas para desarrollar el proyecto o la actividad>
## https://grpc.io/docs/languages/python/quickstart/
## https://www.rabbitmq.com/getstarted.html
## https://flask.palletsprojects.com/en/2.2.x/quickstart/

#### versión README.md -> 1.0 (2022-agosto)
