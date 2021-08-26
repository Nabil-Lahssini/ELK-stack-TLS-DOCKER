import docker

def getContainerID(container):
    client = docker.from_env()
    if client.containers.list(filters={'name': container}):
        response = client.containers.list(filters={'name': container})
        return str(response[0].id)[:12]
    else:
        return None

