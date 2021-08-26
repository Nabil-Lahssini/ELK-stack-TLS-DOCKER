class Heartbeat:
    def __init__(self,code, origin, timestamp, nameService, CPUload, RAMload):
        self.code = code
        self.origin = origin
        self.timestamp = timestamp
        self.nameService = nameService
        self.CPUload = CPUload
        self.RAMload = RAMload