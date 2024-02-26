import pika


conection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

ch = conection.channel()

ch.exchange_declare(exchange="direct_logs", exchange_type="direct")

result = ch.queue_declare(queue="", exclusive=True)
qname = result.method.queue

severities = ("info", "warning", "error")

for severity in severities:
    ch.queue_bind(exchange="direct_logs", queue=qname, routing_key=severity)

print(" [*] Waiting for logs. To exit press CTRL+C")

def callback(ch, method, properties, body):
    print(f"{method.routing_key}, {body}")

ch.basic_consume(queue=qname, on_message_callback=callback, auto_ack=True)

ch.start_consuming()