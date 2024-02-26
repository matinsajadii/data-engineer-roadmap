import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

ch1 = connection.channel()

ch1.queue_declare(queue="hello")

def callback(ch, mehtod, properties, body):
    print(f"recive {body}")

ch1.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)

print("waiting new message, for stoping 'ctrl+c'")

ch1.start_consuming()