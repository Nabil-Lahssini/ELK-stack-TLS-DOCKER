import pika ,sys ,os ,time
from parseXML import parse

QUEUE_MONITORING = os.getenv('QUEUE_LOGGING', 'logging')
print(QUEUE_MONITORING)
filePath = "/logs/logging.log"
if os.path.exists(filePath):
    os.remove(filePath)
f = open(filePath, "a")
f.write('\n')
f.close()
time.sleep(20)


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_MONITORING)
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        f = open(filePath, "a")
        msg = parse(body.decode("utf-8"))
        f.write(msg + '\n')
        f.close()
    channel.basic_consume(
        queue=QUEUE_MONITORING, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()
    connection.close()

if __name__ == '__main__':
    while 1:
        try:
            main()
        except:
            print("Error, retrying in 5 seconds...")
            time.sleep(5)

