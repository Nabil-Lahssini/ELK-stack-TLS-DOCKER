from xmlObject import Heartbeat
import xml.etree.ElementTree as ET


def parse(data):
    try:
        myroot = ET.fromstring(data)
        dataArray = []
        for elements in myroot:
            for x in elements:
                dataArray.append(x.text)
        result = Heartbeat(dataArray[0], dataArray[1], dataArray[2], dataArray[3], dataArray[4], dataArray[5])
        return format(result)
    except Exception:
        return Heartbeat(str(0),str(0),str(0),str(0),str(0),str(0))

def format(data):
    new_data = "{}:{} - {} - {} - {} - {}".format(data.origin, data.nameService, data.timestamp ,data.RAMload, data.CPUload, data.code)
    return new_data

