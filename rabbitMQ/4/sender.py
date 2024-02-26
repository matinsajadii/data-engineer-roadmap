import pika


conection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

ch = conection.channel()

ch.exchange_declare(exchange="direct_logs", exchange_type="direct")

messages = {
    "info": "this is INFO message",
    "warning": "this is WARNING message",
    "error": "this is ERROR message",
}

print("sent message!")

for k,v in  messages.items():
    ch.basic_publish(exchange="direct_logs", routing_key=k, body=v)

conection.close()