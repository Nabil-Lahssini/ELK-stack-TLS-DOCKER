# ELK-stack on Docker (HTPPS, TLS)
Elastic stack with RabbitMQ instance. Custom heartbeat service written in Python.

## Start
To start and configure the service for the first time:
```
bash startup.sh
```
## Stop
```
docker-compose down
```
### Stop and delete the volumes
```
docker-compose down -v
```
