import pika

connetion = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

ch1 = connetion.channel()

ch1.queue_declare(queue="hello")

ch1.basic_publish(exchange="", routing_key="hello", body="Hello World!")
print(f"message sent")

connetion.close()