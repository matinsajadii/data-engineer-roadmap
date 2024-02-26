import time

import pika

conection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

ch = conection.channel()

ch.queue_declare(queue="first", durable=True)

def callback(ch, method, properties, body):
    print(f"recive {body}")
    print(method)
    time.sleep(9)
    print("done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

ch.basic_qos(prefetch_count=1)
ch.basic_consume(queue="first", on_message_callback=callback)

print("wating for message, press 'ctrl+c' to exit")

ch.start_consuming()