from xmlObject import Log
import xml.etree.ElementTree as ET

def parse(data):
    try:
        myroot = ET.fromstring(data)
        dataArray = []
        for elements in myroot:
            for x in elements:
                dataArray.append(x.text)
        result = Log(dataArray[0], dataArray[1], dataArray[2], dataArray[3], dataArray[4], dataArray[5], dataArray[6])
        return format(result)
    except Exception:
        return Log(str(0),str(0),str(0),str(0),str(0),str(0))

def format(data):
    new_data = "{} - {} - {} - {} - {} - {} - {}".format(data.code, data.origin, data.timestamp ,data.objectUUID, data.objectSourceId, data.objectOrigin, data.description)
    return new_data