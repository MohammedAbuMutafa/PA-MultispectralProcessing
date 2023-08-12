from datetime import datetime


class IncomingMessageDTO:

    def __init__(self,
                 id: str,
                 fileName: str,
                 dt_processed,
                 ):
        self.id = id
        self.fileName = fileName
        self.dt_processed = dt_processed
