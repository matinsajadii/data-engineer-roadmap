import pika
import uuid


class Sender:
    def __init__(self) -> None:
        self.conection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
        self.channel = self.conection.channel()
        result = self.channel.queue_declare(queue="", exclusive=True)
        self.qname = result.method.queue
        self.channel.basic_consume(queue=self.qname, on_message_callback=self.on_response, auto_ack=True)

    def on_response(self, ch, mthod, proper, body):
        if self.corr_id == proper.correlation_id:
            self.response = body


    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange="",
            routing_key="rpc_queue",
            properties=pika.BasicProperties(reply_to=self.qname, correlation_id=self.corr_id),
            body=str(n)
        )

        while self.response is None:
            self.conection.process_data_events()

        return int(self.response)


send = Sender()

response = send.call(30)

print(response)