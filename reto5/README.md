# info de la materia: ST0263
# Estudiante(s): Daniel Arango Hoyos, darangoh@eafit.edu.co
# Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
# Laboratorio 5: Big Data
#
# Lab 5.1-aws-emr
#
Se crea el cluster en EMR y se le configuran los parámetros necesarios:
![Captura desde 2023-05-10 11-12-16](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/e2495588-01ec-4f01-afcd-11935a0684e3)

![Captura desde 2023-05-10 11-12-41](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/44762a8e-7cdb-4032-b2ed-a288396a0de5)

![Captura desde 2023-05-10 11-13-19](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/e71d9087-2183-4417-bfad-b705e17a9e4d)

![Captura desde 2023-05-10 11-14-20](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/ce8cb232-2926-4077-a2cb-75e40a4080b6)

![Captura desde 2023-05-10 11-15-16](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/5dcad738-e674-435e-b5ac-947a512c9fbc)

![Captura desde 2023-05-10 11-17-04](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/cb2be5e2-a4c2-44a5-9140-701aaad53b3e)

Una vez todos los parámetros configurados, hay que esperar entre 20-25 minutos a que se inicialice el cluster:
![Captura desde 2023-05-10 12-03-44](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/2a139352-1ddd-457b-a1d7-b2b128dbf312)

Ya cuando se haya inicializado el cluster, se procederá a modificar los puertos de acceso público y las reglas de seguridad para permitir el funcionamiento de las siguientes aplicaciones (HDFS Name Node, Hue, JupyterHub, Zeppelin):
![image](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/d846ce8f-46c2-4301-962d-aeba2ab90019)

Y también el puerto 22 para permitir el control de la instancia principal mediante SSH:
![Captura desde 2023-05-10 23-38-34](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/8443a666-b4f0-4d48-bcce-03c92de952a6)
![Captura desde 2023-05-10 23-39-46](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/05333221-863b-4d3c-a1ae-48c2051e500a)
![Captura desde 2023-05-10 23-39-52](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/ba457326-7e8c-4b92-9bb9-d46f8022b3c0)

Ya abiertos dichos puertos, se procede a verificar el acceso a las aplicaciones mencionadas:

Hue:
![Captura desde 2023-05-10 21-15-54](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/3f74e0d4-be34-4d59-91d8-807eaf7b8735)
(En Hue nos registramos con el username de hadoop).

![Captura desde 2023-05-10 21-20-24](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/4cf5e495-c040-4040-8573-b45d15295c3c)

JupyterHub:

![Captura desde 2023-05-10 21-19-51](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/39550655-49d1-47d6-9f6a-24ce9822c6e1)
(en jupyterhub el usuario para ingresar es jovyan y la contraseña es jupyter).

![Captura desde 2023-05-10 21-20-16](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/e0611bd3-4dee-40ab-83fb-3055bed78456)

![Captura desde 2023-05-10 21-24-28](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/86e70d3d-4cf9-42b6-b8ee-9bf0beddfcbf)
(Se hace un script para iniciar Spark).

![Captura desde 2023-05-10 21-28-24](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/54516615-c021-4d96-9d75-9422f59fc483)

Zeppelin:

![Captura desde 2023-05-10 21-30-49](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/f608844a-c918-4cf0-8792-d884dca3737b)

Y luego de verificar que se puede acceder a todas las aplicaciones necesarias procedemos a ingresar a la consola de la instancia principal:

![Captura desde 2023-05-10 21-17-45](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/91a2092d-d9a0-4d8a-837f-992abea02bc0)

![Captura desde 2023-05-10 21-17-59](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/21d99f1a-a901-4f47-8e2a-fd3c1c3b086b)

# Lab 5.2-hdfs-s3
#
Para este laboratorio empezamos creando un Bucket con S3 para poder almacenar los datasets que utilizaremos:

![Captura desde 2023-05-10 23-28-58](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/a8ccbb47-971f-4099-9cf5-0eafcc78f5b7)

Y también tendremos que configurar dentro de la terminal conectada a la instancia principal el puerto que se conecta al hue para permitir que este último pueda tener constancia de los archivos que se van almacenando en el cluster, por lo que se accede al archivo de configuración de Hue `sudo nano /etc/hue/conf.empty/hue.ini` y buscamos 14000:

![Captura desde 2023-05-10 23-15-15](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/fee0c9b6-12fd-4979-9577-1d6718cee6bb)
(por defecto está el 14000 pero en la imagen ya está cambiado al 9870, que es por el que escucha la aplicación HDFS Name Node)

Luego de realizar este cambio, procedemos a reiniciar el Hue con el comando `sudo systemctl restart hue.service`.

Con esto ya configurado, continuamos importando los datasets desde el directorio s3 `s3://st0263darangoh/datasets`:

![Captura desde 2023-05-10 22-49-57](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/2824a5cd-83f1-46d8-9d6e-91740b53831f)
![image](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/fff65f63-be79-48b2-98a2-51e786e34e7f)

Y verificamos en Hue:

![Captura desde 2023-05-10 23-29-51](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/4020fb55-7843-4360-9cd4-d1f7cd36e7d8)

Luego, procedemos a importar los datasets locales a un nuevo directorio s3 nombrado `s3://st0263darangoh/darangoh/datasets`:

![Captura desde 2023-05-11 00-02-34](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/8c05d73e-0ee7-43de-91b5-76d877e44cca)

Y lo verificamos en S3: 
![Captura desde 2023-05-10 23-28-47](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/1e54d56e-6e59-4212-9c74-4c8835b9956c)

