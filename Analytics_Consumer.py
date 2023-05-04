import pika
from pika.exchange_type import ExchangeType

def callback(ch, method, properties, body):
    print(f"Setor de Analytics recebeu a mensagem: {body.decode()}")

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)
channel.exchange_declare(exchange='direct-ex', exchange_type=ExchangeType.direct)

result = channel.queue_declare(queue='', exclusive=True)

queue_name = result.method.queue

#channel.queue_bind(exchange='pubsub', queue=queue_name)
channel.queue_bind(exchange='direct-ex', queue=queue_name, routing_key='analytics')

print(' [*] Esperando mensagens. Para sair aperte CTRL+C')
    
channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

print("Consumindo mensagens da fila...")

channel.start_consuming()