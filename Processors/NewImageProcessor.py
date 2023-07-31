from Modules.VegetationIndex.Multispectral import Multispectral
from Modules.Messaging.MessageReceiver import MessageReceiver
from Modules.Messaging.MessageSender import MessageSender
from dto.IncomingMessageDTO import IncomingMessageDTO
import logging
import json
import matplotlib.pyplot as plt


class NewImageProcessor():

    def __init__(self):

        self.__init_logger__()
        self.multispectral = Multispectral()

        self.message_receiver = MessageReceiver()
        # self.message_sender = MessageSender()
        self.message_receiver.start(self.handle_new_message)

    def __init_logger__(self):
        logging.getLogger("matplotlib").setLevel(logging.WARNING)
        logging.getLogger("PIL").setLevel(logging.WARNING)
        self.logger = logging.getLogger('Main.Processor')
        self.logger.setLevel(logging.DEBUG)

    def handle_new_message(self, ch, method, properties, body):

        body_json = json.loads(body.decode())
        message = IncomingMessageDTO(
            fileName=body_json['fileName'], DateTimeProcessed=body_json['DateTimeProcessed'])
        self.logger.info(f"[x] New file recieved: {message.fileName}")

        self.process_message(message)

    def process_message(self, new_image: IncomingMessageDTO):
        ndvi = self.multispectral.ndvi(new_image.fileName)
        self.plotResult(ndvi)

    def plotResult(self, img, save=False):
        fig = plt.figure()
        plt.imshow(img, cmap=('RdYlGn'))
        plt.colorbar()
        plt.show()
