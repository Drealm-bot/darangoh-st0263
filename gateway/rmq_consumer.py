import pika
import uuid

rmq_host = "localhost"
rmq_port = 5672
rmq_vhost = "/"
rmq_user = "guest"
rmq_password = "guest"
rmq_queue = "search_file_queue"

class RMQConsumer:

    def __init__(self):
        rmq_credentials = pika.PlainCredentials(rmq_user, rmq_password)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=rmq_host, port=rmq_port, virtual_host=rmq_vhost, credentials=rmq_credentials))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=rmq_queue)
        result = self.channel.queue_declare('', exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(queue=self.callback_queue,
                                   on_message_callback=self.on_response,
                                   auto_ack=True)
        
    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body.decode('utf-8')
    
    def call(self, text):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key=rmq_queue,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=text)
        while self.response is None:
            self.connection.process_data_events()
        return self.response
