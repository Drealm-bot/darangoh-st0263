import pika
import os

rmq_host = "localhost"
rmq_port = 5672
rmq_vhost = "/"
rmq_user = "guest"
rmq_password = "guest"
rmq_queue = "search_file_queue"
dir = "/home/ubuntu/darangoh-st0263/dir"

rmq_credentials = pika.PlainCredentials(rmq_user, rmq_password)
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rmq_host, port=rmq_port, virtual_host=rmq_vhost, credentials=rmq_credentials))
#connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue=rmq_queue)

#current_dir = os.path.abspath(os.curdir)
#dir_path = os.path.abspath(os.path.join(current_dir, "dir"))

def search_files(text):
    for files in os.walk(dir):
        print(files)
        for file in files:
            print(file)
            if text in file:
                return f"El archivo {text} ha sido hallado."
    return f"No se ha hallado el archivo {text}."

def on_request(ch, method, props, body):
    
    text = body.decode()

    
    results = search_files(text)

    
    response = ','.join(results)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = props.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=rmq_queue, on_message_callback=on_request)


print("Esperando por mensajes...")
channel.start_consuming()
