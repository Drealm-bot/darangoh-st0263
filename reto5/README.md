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

# Lab 5.3-spark

#__Parte 1__
Scripts:
https://github.com/Drealm-bot/darangoh-st0263/blob/main/reto5/MrScripts/AvgSalary.py
https://github.com/Drealm-bot/darangoh-st0263/blob/main/reto5/MrScripts/Movies.py
https://github.com/Drealm-bot/darangoh-st0263/blob/main/reto5/MrScripts/Stocks.py

#__Parte 2__
Se conecta al nodo master y se inicializa spark para ejecutar los siguientes comandos:
![Captura desde 2023-05-18 19-38-28](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/1aa3dbd8-1484-4707-8889-e6efd93d7db0)

Resultados y se guardan en el hdfs:
![Captura desde 2023-05-18 19-38-49](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/ece12a54-e4a7-4607-be0d-31ed82d99899)

Se realiza lo mismo pero utilizando los datasets ubicados en el bucket s3://st0263darangoh/ y almacenando los resultados en s3://st0263darangoh/darangoh:
![image](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/ba999e92-bcaf-4368-b77f-c74666bb7369)

Ahora se procede a realizar la misma operación pero esta vez desde Jupyter:
![Captura desde 2023-05-18 19-56-55](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/127df810-2dbf-42b9-a947-c5e3bce054d6)

Y se guarda en el bucket s3 como el ejemplo ejecutado en el nodo master del emr:
![Captura desde 2023-05-18 19-57-06](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/151d38a8-0c3f-44c0-9173-efda7f9c1368)

Y se ve que se almacenó en el bucket como el ejemplo pasado:
![image](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/c078dc6a-ef96-4069-a5ac-2ce4da850cf6)

#Replicación del notebook en Jupyter
![Captura desde 2023-05-18 20-22-55](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/29f7071c-bc84-4c0d-8678-f12932d0e1a7)
![Captura desde 2023-05-18 20-23-05](https://github.com/Drealm-bot/darangoh-st0263/assets/61467004/5204250a-0465-4f82-a114-c90d534e87db)

Bloque 3-4: Se crea y asigna una sesión de Spark.

Bloque 5: Se lee el archivo de datos desde S3 's3://st0263darangoh/datasets/sample_data.csv'.

Bloques 6-7: Se muestran las columnas y sus longitudes.

Bloque 7: Se muestra el número de filas.

Bloque 8: Se muestra la forma de los datos.

Bloque 9: Se imprime el esquema.

Bloque 10: Se consultan e imprimen las primeras cinco filas.

Bloque 11: Se consultan e imprimen las primeras cinco filas, mostrando solo las columnas de edad y móvil.

Bloque 12: Se imprimen algunas estadísticas sobre el dataframe.

Bloque 13: Se importan algunos tipos de SQL.

Bloque 14: Se agrega una nueva columna llamada "age_after_10_yrs" al DataFrame tomando los valores de la columna existente "age" y sumándoles 10 a cada valor. Finalmente, se muestran las primeras 10 filas del DataFrame modificado, con la opción de deshabilitar la truncación para mostrar el contenido completo de cada fila.

Bloque 15: Se agrega una nueva columna llamada "age_double" al DataFrame convirtiendo los valores de la columna existente "age" a un tipo de datos Double utilizando la función cast(). La función cast() se utiliza para cambiar el tipo de datos de una columna. Finalmente, se muestran las primeras 10 filas del DataFrame modificado, con la opción de deshabilitar la truncación para mostrar el contenido completo de cada fila.

Bloque 16: Se agrega una nueva columna llamada "age_after_10_yrs" al DataFrame tomando los valores de la columna existente "age" y sumándoles 10 a cada valor. Esta nueva columna representa la edad de cada individuo después de 10 años. Finalmente, se muestran las primeras 10 filas del DataFrame modificado, con la opción de deshabilitar la truncación para mostrar el contenido completo de cada fila.

Bloque 17: Se filtra el DataFrame df en base a una condición. Específicamente, se seleccionan las filas donde el valor en la columna "mobile" es igual a "Vivo". Se utiliza el método filter() para aplicar la condición, y df['mobile']=='Vivo' crea una expresión booleana que verifica si el valor en la columna "mobile" es igual a "Vivo". Finalmente, se llama al método show() para mostrar el DataFrame filtrado resultante, mostrando todas las filas que cumplen la condición.

Bloque 18: Se filtra el DataFrame df en base a una condición donde el valor en la columna "mobile" es igual a "Vivo". Luego se seleccionan columnas específicas, en este caso "age", "ratings" y "mobile", del DataFrame filtrado. Finalmente, se muestra el DataFrame resultante, mostrando solo las columnas seleccionadas para las filas que cumplen la condición.

Bloque 19: Se filtra el DataFrame df para seleccionar las filas donde el valor en la columna "mobile" es igual a "Vivo" y el valor en la columna "experience" es mayor que 10. Se aplican múltiples filtros de forma secuencial para reducir el conjunto de datos. Finalmente, se muestra el DataFrame resultante, mostrando todas las columnas para las filas filtradas que cumplen ambas condiciones.

Bloque 20: Se filtra el DataFrame df para seleccionar las filas que cumplen dos condiciones simultáneamente. La primera condición verifica si el valor en la columna "mobile" es igual a "Vivo", y la segunda condición verifica si el valor en la columna "experience" es mayor que 10. El operador & combina estas dos condiciones mediante el operador lógico AND. El DataFrame resultante solo incluirá filas donde se cumplan ambas condiciones.

Bloque 21: Se selecciona la columna "mobile" del DataFrame df. Luego se aplica la función distinct(), que elimina los valores duplicados, asegurando que solo se retengan los valores únicos. Finalmente, se muestran los valores distintos en la columna "mobile".

Bloque 22: Se selecciona la columna "mobile" del DataFrame df. Luego se aplica la función distinct(), que elimina los valores duplicados, asegurando que solo se retengan los valores únicos. Finalmente, se llama a la función count() para calcular el número de valores distintos en la columna "mobile".

Bloque 23: Se agrupa el DataFrame df por los valores en la columna "mobile". Luego se calcula el conteo de ocurrencias para cada marca de móvil única utilizando la función count(). Finalmente, se muestra el DataFrame agrupado resultante, mostrando la marca de móvil y su conteo correspondiente.

Bloque 24: Se agrupa el DataFrame df por los valores en la columna "mobile". Luego se calcula el conteo de ocurrencias para cada marca de móvil única utilizando la función count(). A continuación, se ordena el DataFrame agrupado resultante en orden descendente basado en la columna "count" utilizando la función orderBy().

Bloque 25: Se agrupa el DataFrame df por los valores en la columna "mobile". Luego se calcula el valor promedio (media) para cada columna numérica en el DataFrame agrupado utilizando la función mean().

Bloque 26: Se agrupa el DataFrame df por los valores en la columna "mobile". Luego se calcula la suma de cada columna numérica dentro de cada grupo utilizando la función sum().

Bloques 27-28: Se agrupa el DataFrame df por los valores en la columna "mobile". Luego se calcula el valor máximo/mínimo para cada columna numérica dentro de cada grupo utilizando las funciones min()/max().

Bloque 29: Se agrupa el DataFrame df por los valores en la columna "mobile". Luego se aplica la función agg() para calcular una agregación en una columna específica. En este caso, se calcula la suma de la columna "experience" dentro de cada grupo.

Bloque 30-32: Se aplica una función definida por el usuario (UDF) llamada brand_udf a la columna 'mobile' de un DataFrame df. Esta UDF transforma los valores en la columna 'mobile' y agrega una nueva columna llamada 'price_range' al DataFrame. Finalmente, el código muestra las primeras 10 filas del DataFrame modificado, mostrando las columnas originales junto con la columna recién agregada 'price_range'.

Bloque 33: Se define una función definida por el usuario (UDF) utilizando una función lambda. La UDF se llama age_udf y toma una 'edad' como entrada. Devuelve "joven" si la edad es menor o igual a 30, y "mayor" en caso contrario. El tipo de retorno se especifica como StringType(). Luego, se aplica la UDF al DataFrame df utilizando la función withColumn(). Se agrega una nueva columna llamada 'age_group' al DataFrame aplicando la función age_udf a la columna 'edad'.

Bloque 36: Desafortunadamente, jupyterhub se quejaba de que no estaba instalado Pandas >= 1.0.5 y no pude resolver este problema. Por lo tanto, no pude ejecutar la sección de pandas.

Bloque 38-43: Todo este código está relacionado con guardar los resultados en AWS S3.
