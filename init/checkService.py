import requests, time
def checkES():
    URL = "https://localhost:9200/_status"
    status = False
    while status is False:
        try:
            response = requests.get(url = URL, verify=False)
            print(response.status_code)
            if response.status_code == 401:
                print("ok")
                status = True
            else:
                print("ES still not up, trying again in 5 sec...")
                time.sleep(5)
        except:
            print("ES still not up, trying again in 3 sec...")
            time.sleep(3)