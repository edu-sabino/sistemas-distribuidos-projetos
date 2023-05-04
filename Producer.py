import pika
from pika.exchange_type import ExchangeType

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)
channel.exchange_declare(exchange='direct-ex', exchange_type=ExchangeType.direct)

message = "Novo cliente cadastrado: {nome: 'Marcos Sales', idade: 44, endereço: 'Rua Tales Neves, 458 - Campinas - SP', interesses: ['Python', 'Angular', 'Django']}"

#channel.basic_publish(exchange='pubsub', routing_key='', body=message)
channel.basic_publish(exchange='direct-ex', routing_key='analytics', body=message)
    
print(" [x] Enviado: %r" % message)

connection.close()