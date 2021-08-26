import pika,time, json
from datetime import datetime
from random import seed
from random import randint
seed(1)
arrCode = [1000,2000,3000,4000,5000]
arrOrigin = ["office", "AD", "Frontend", "Canvas"]
def getusage():
    code = arrCode[randint(0, 3)]
    origin = arrOrigin[randint(0, 3)]
    data = """
    <error>
  <header>
    <code>{}</code>
    <origin>{}</origin>
    <timestamp>{}</timestamp>
  </header>
  <body>
    <objectUUID>333ade47-03d1-40bb-9912-9a6c86a60169</objectUUID>
    <objectSourceId>{}</objectSourceId>
    <objectOrigin>{}</objectOrigin>
    <description>Object does not follow XSD pattern</description>
  </body>
</error>""".format(code,origin, datetime.now(), randint(0,500) ,origin)
    return data


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    while(1):
        msg = getusage()
        channel.basic_publish(exchange='',
                            routing_key='logging',
                            body=msg, )
        print(" [x] Sent Error")
        time.sleep(5)
    connection.close()

while(1):
  try:
    main()
  except:
    print("RMQ offline")
    print("retrying in 5 seconds...")
    time.sleep(5)
