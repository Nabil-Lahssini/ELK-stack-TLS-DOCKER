import requests, docker, pytest, os, time
# insert at 1, 0 is the script path (or '' in REPL)
import ressources.hbXML as hbXML
import ressources.logXML as logXML

def test_heartbeatparse():
    xmltest = """
        <heartbeat> 
            <header> 
                <code>2000</code> 
                <origin>FrontEnd</origin> 
                <timestamp>2021-05-25T12:00:00+01:00</timestamp> 
            </header> 
            <body> 
                <nameService>Website</nameService> 
                <CPUload>5.63</CPUload> 
                <RAMload>86.13</RAMload> 
            </body> 
        </heartbeat> """
    result = hbXML.parse(xmltest)
    assert result == "FrontEnd:Website - 2021-05-25T12:00:00+01:00 - 86.13 - 5.63 - 2000" 
def test_logparse():
    xmltest = """
        <error>
  <header>
    <code>1005</code>
    <origin>AD</origin>
    <timestamp>2021-05-25T12:00:00+01:00</timestamp>
  </header>
  <body>
    <objectUUID>333ade47-03d1-40bb-9912-9a6c86a60169</objectUUID>
    <objectSourceId>22</objectSourceId>
    <objectOrigin>FrontEnd</objectOrigin>
    <description>Object does not follow XSD pattern</description>
  </body>
</error>"""
    result = logXML.parse(xmltest)
    assert result == "1000 - AD - 2021-05-25T12:00:00+01:00 - 333ade47-03d1-40bb-9912-9a6c86a60169 - 22 - FrontEnd - Object does not follow XSD pattern" 

def test_runningcontainers():
    client = docker.from_env()
    if client.containers.list(all=True):
        assert len(client.containers.list(all=True)) >= 7
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
