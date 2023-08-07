from Modules.VegetationIndex.Multispectral import Multispectral
from Modules.Messaging.NewImageReceiver import NewImageReceiver
from dto.IncomingMessageDTO import IncomingMessageDTO
import logging
import json
import matplotlib.pyplot as plt


class NewImageProcessor():

    def __init__(self):
        self.__init_logger__()
        self.multispectral = Multispectral()
        self.message_receiver = NewImageReceiver(
            self.handle_new_message)

    def __init_logger__(self):
        logging.getLogger("matplotlib").setLevel(logging.WARNING)
        logging.getLogger("PIL").setLevel(logging.WARNING)
        self.logger = logging.getLogger('Main.Processor')
        self.logger.setLevel(logging.DEBUG)

    def handle_new_message(self, ch, method, properties, body):
        body_json = json.loads(body.decode())

        message = IncomingMessageDTO(
            fileName=body_json['fileName'],
            dt_processed=body_json['dt_processed'],
            red_e_image=body_json['red_e_image'],
            red_image=body_json['red_image'],
            green_image=body_json['green_image'],
            nir_image=body_json['nir_image'])

        self.logger.info(f"[x] New file recieved: {message.fileName}")

        self.process_message(message)

    def process_message(self, new_image: IncomingMessageDTO):
        self.logger.info("Recieved !")
        

    def plotResult(self, img, save=False):
        fig = plt.figure()
        plt.imshow(img, cmap=('RdYlGn'))
        plt.colorbar()
        plt.show()
