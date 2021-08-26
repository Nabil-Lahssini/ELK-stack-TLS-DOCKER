from manage import getContainerID
from parse import save, parse
from checkService import checkES
import os, time
filePaths = ["login.txt", "temp.txt"]
for files in filePaths:
    if os.path.exists(files):
        os.remove(files)

os.system("cd .. && docker-compose down -v")
os.system("cd .. && sudo docker-compose -f create-certs.yml run --rm create_certs")
os.system("cd .. && docker-compose up -d")
print("waiting for ELK to start up...")
checkES()
id = getContainerID("monitoring_es01_1")
os.system('sudo docker exec {} /bin/bash -c "bin/elasticsearch-setup-passwords auto --batch --url https://localhost:9200" >> ./temp.txt'.format(id,))
output = ""
with open(filePaths[1], "r") as ping:
    output = ping.read()
result = save(output)
print("done !")