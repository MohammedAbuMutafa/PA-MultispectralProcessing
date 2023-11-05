from Enums.MultiSpectralEnum import MultiSpectralEnum
from Modules.DirectoryManager import DirectoryManager
from dto.IncomingMessageDTO import IncomingMessageDTO
import numpy as np
import matplotlib.pyplot as plt
import os


class ImageSaver():
    def __init__(self) -> None:
        self.directory_manager = DirectoryManager()
        self.directory_manager.create_session_dirs()

    def save_image(self, img, image_details: IncomingMessageDTO, processing_type: MultiSpectralEnum, use_color_bar=False):
        self.save_image_as_jpg(img, image_details, processing_type)
        self.save_image_as_np_file(img, image_details, processing_type)
        if (os.getenv('DEBUG_MODE') == 'TRUE'):
            self.save_debug_image(img, image_details, processing_type)

    def save_debug_image(self, img, image_details: IncomingMessageDTO, processing_type: MultiSpectralEnum):
        fig = plt.figure(figsize=(7.50, 7.50), dpi=100)
        plt.imshow(img)
        plt.colorbar()
        output_dir = self.directory_manager.session_dir
        file = os.path.join(output_dir, processing_type.name, "debug",
                            image_details.fileName)
        fig.savefig(file, dpi=100)
        plt.close(fig)

    def save_image_as_jpg(self, img, image_details: IncomingMessageDTO, processing_type: MultiSpectralEnum):
        fig = plt.figure(frameon=False, figsize=(7.50, 7.50), dpi=100)
        ax = plt.Axes(fig, [0., 0., 1., 1.])
        ax.set_axis_off()
        fig.add_axes(ax)
        # plt.imshow(img, cmap=('RdYlGn'))
        plt.imshow(img)
        output_dir = self.directory_manager.session_dir
        file = os.path.join(output_dir, processing_type.name, "images",
                            image_details.fileName)
        fig.savefig(file, bbox_inches='tight', pad_inches=0.0, dpi=100)
        plt.close(fig)

    def save_image_as_np_file(self, img, image_details: IncomingMessageDTO, processing_type: MultiSpectralEnum):

        file_name = image_details.fileName.replace(".jpg", ".txt")
        output_dir = self.directory_manager.session_dir
        final_output_path = os.path.join(
            output_dir, processing_type.name, "numpy", file_name)

        np.savetxt(final_output_path, img)
