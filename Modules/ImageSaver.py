from Enums.MultiSpectralEnum import MultiSpectralEnum
from Modules.DirectoryManager import DirectoryManager
from dto.IncomingMessageDTO import IncomingMessageDTO
import matplotlib.pyplot as plt
import os


class ImageSaver():
    def __init__(self) -> None:
        self.directory_manager = DirectoryManager()
        self.directory_manager.create_session_dirs()

    def save_image(self, img, image_details: IncomingMessageDTO, processing_type: MultiSpectralEnum, use_color_bar=False):
        fig = plt.figure(frameon=False, figsize=(7.50, 7.50), dpi=100)
        ax = plt.Axes(fig, [0., 0., 1., 1.])
        ax.set_axis_off()
        fig.add_axes(ax)
        plt.imshow(img, cmap=('RdYlGn'))
        if (use_color_bar):
            plt.colorbar()
        output_dir = self.directory_manager.session_dir
        file = os.path.join(output_dir, processing_type.name,
                            image_details.fileName)
        fig.savefig(file, bbox_inches='tight', pad_inches=0.0, dpi=100)
        plt.close(fig)
