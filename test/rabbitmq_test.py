import pika, pytest
# command: python3 -m pytest test1.py

QUEUE_MONITORING = 'QUEUE_MONITORING'
RABBITMQ_HOST = 'localhost'

def test_rabbitmq_publish():
    x=0
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_MONITORING)
    channel.basic_publish(exchange='', routing_key=QUEUE_MONITORING, body='Hello!')
    x=1
    connection.close()
    assert x == 1



def test_rabbitmq_consume():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()

    for method_frame, properties, body in channel.consume(QUEUE_MONITORING):
        channel.basic_ack(method_frame.delivery_tag)
        assert body != None    
        if method_frame.delivery_tag == 1:
            requeued_messages = channel.cancel()
            channel.close()
            connection.close()
            break


def test_rabbitmq_connectivity():
    URL = 'amqp://guest:guest@localhost:5672/%2F'
    parameters = pika.URLParameters(URL)
    try:
        connection = pika.BlockingConnection(parameters)
        assert connection.is_open
            
    except Exception as error:
        assert False


  

