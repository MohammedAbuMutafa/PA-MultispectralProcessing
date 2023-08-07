from datetime import datetime


class IncomingMessageDTO:

    def __init__(self,
                 fileName: str,
                 dt_processed,
                 red_image,
                 nir_image,
                 green_image,
                 red_e_image,
                 ):
        self.fileName = fileName
        self.dt_processed = dt_processed
        self.red_image = red_image
        self.nir_image = nir_image
        self.green_image = green_image
        self.red_e_image = red_e_image
