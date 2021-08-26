import xml.etree.ElementTree as ET

class Log:
    def __init__(self,code, origin, timestamp, objectUUID, objectSourceId, objectOrigin, description):
        self.code = round(int(code), -3)
        self.origin = origin
        self.timestamp = timestamp
        self.objectUUID = objectUUID
        self.objectSourceId = objectSourceId
        self.objectOrigin = objectOrigin
        self.description = description

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

