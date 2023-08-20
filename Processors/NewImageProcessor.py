from Modules.VegetationIndex.MultispectralFactory import MultispectralFactory
from Modules.Messaging.NewImageReceiver import NewImageReceiver
from dto.IncomingMessageDTO import IncomingMessageDTO
import logging
import json
import matplotlib.pyplot as plt
from PIL import Image
from Exceptions.ImageDtoMapException import ImageDtoMapException
from Modules.DirectoryManager import DirectoryManager
from Enums.MultiSpectralEnum import MultiSpectralEnum
import os


class NewImageProcessor():

    def __init__(self):
        self.__init_logger__()
        self.directory_manager = DirectoryManager()
        self.directory_manager.create_session_dirs()
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
            self.logger.info(
                f"Processing {new_image.fileName} in {multispectral_index.name} index")
            image = self.multispectral.process(
                new_image.fileName, multispectral_index)
            self.save_image(image, new_image,
                            processing_type=multispectral_index)

    def save_image(self, img, image_details: IncomingMessageDTO, processing_type: MultiSpectralEnum, use_color_bar=False):
        fig = plt.figure(frameon=False)
        ax = plt.Axes(fig, [0., 0., 1., 1.])
        ax.set_axis_off()
        fig.add_axes(ax)
        plt.imshow(img, cmap=('RdYlGn'))
        if (use_color_bar):
            plt.colorbar()
        output_dir = self.directory_manager.processed_dir
        file = os.path.join(output_dir, processing_type.name,
                            image_details.fileName)
        fig.savefig(file)
        plt.close(fig)
