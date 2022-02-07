import requests, docker, pytest, os, time

def test_runningcontainers():
    client = docker.from_env()
    if client.containers.list(all=True):
        assert len(client.containers.list(all=True)) >= 4
    else:
        assert False

def test_es_running():
    for i in range(20):
        try:
            response = requests.get('https://localhost:9200', verify=False)
            break          
        except:
            time.sleep(3)
    assert response.status_code == 401
