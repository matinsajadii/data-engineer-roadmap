import pika

conection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

ch = conection.channel()

ch.queue_declare(queue="first", durable=True)

message = "this is testing message"

ch.basic_publish(exchange="",
                 routing_key="first",
                 body=message,
                 properties=pika.BasicProperties(delivery_mode=2, headers={"sina": "nazi"})
)

print("messages sent")

conection.close()