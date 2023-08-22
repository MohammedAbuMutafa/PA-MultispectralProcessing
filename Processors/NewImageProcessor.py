from Modules.ImageSaver import ImageSaver
from Modules.VegetationIndex.MultispectralFactory import MultispectralFactory
from Modules.Messaging.NewImageReceiver import NewImageReceiver
from dto.IncomingMessageDTO import IncomingMessageDTO
import logging
import json
import matplotlib.pyplot as plt
from Exceptions.ImageDtoMapException import ImageDtoMapException
from Modules.DirectoryManager import DirectoryManager
from Enums.MultiSpectralEnum import MultiSpectralEnum
import os


class NewImageProcessor():

    def __init__(self):
        self.__init_logger__()
        self.image_saver = ImageSaver()
        self.multispectral = MultispectralFactory()
        self.message_receiver = NewImageReceiver(
            self.handle_new_message)

    def __init_logger__(self):
        logging.getLogger("matplotlib").setLevel(logging.WARNING)
        logging.getLogger("PIL").setLevel(logging.WARNING)
        self.logger = logging.getLogger('Main.Processor')
        self.logger.setLevel(logging.DEBUG)

    def handle_new_message(self, ch, method, properties, body):
        body_json = json.loads(body.decode())

        try:
            message = IncomingMessageDTO(
                id=body_json['id'],
                fileName=body_json['fileName'],
                dt_processed=body_json['dt_processed'],
            )
        except Exception:
            raise ImageDtoMapException("Unable to map incoming image")

        self.logger.info(
            f"[x] New Image: filename: {message.fileName} \nid: {message.id}")

        self.process_message(message)

    def process_message(self, new_image: IncomingMessageDTO):
        for multispectral_index in MultiSpectralEnum:
            self.__process_image__(new_image, multispectral_index)

    def __process_image__(self, new_image: IncomingMessageDTO, multispectral_index: MultiSpectralEnum):
        self.logger.info(
            f"Processing {new_image.fileName} in {multispectral_index.name} index")
        image = self.multispectral.process(
            new_image.fileName, multispectral_index)
        self.image_saver.save_image(image, new_image,
                                    processing_type=multispectral_index)
