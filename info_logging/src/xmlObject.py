class Log:
    def __init__(self,code, origin, timestamp, objectUUID, objectSourceId, objectOrigin, description):
        self.code = round(int(code), -3)
        self.origin = origin
        self.timestamp = timestamp
        self.objectUUID = objectUUID
        self.objectSourceId = objectSourceId
        self.objectOrigin = objectOrigin
        self.description = description