import pika

conection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

ch = conection.channel()

ch.exchange_declare(exchange="logs", exchange_type="fanout")

ch.basic_publish(exchange="logs", routing_key="", body="this is testing fanout")

print("sent message!")

conection.close()