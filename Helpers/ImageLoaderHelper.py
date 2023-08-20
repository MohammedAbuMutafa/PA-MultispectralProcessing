import os
import rasterio
from Enums.ImageTypeEnum import ImageType
import logging

from Modules.DirectoryManager.DirectoryManager import DirectoryManager


class ImageLoaderHelper():

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        logging.getLogger("rasterio").setLevel(logging.WARNING)
        self.directory_manager = DirectoryManager()
        self.__init_directories__()

    def __init_directories__(self):
        input_directories = self.directory_manager.get_input_dirs()

        self.green_dir = input_directories['GREEN']
        self.nir_dir = input_directories['NIR']
        self.red_dir = input_directories['RED']
        self.red_e_dir = input_directories['RED_EDGE']

    def load(self, file_name: str, image_type: ImageType):

        try:
            file = os.path.join(self.__get_image_type__(image_type), file_name)
            image = rasterio.open(file)
            return image.read(1).astype('float64')
        except ValueError as e:
            self.logger.error(e)
        except Exception:
            raise ValueError("Unable to load file")

    def __get_image_type__(self, image_type: ImageType) -> str:

        match image_type:
            case ImageType.red:
                return self.red_dir
            case ImageType.green:
                return self.green_dir
            case ImageType.nir:
                return self.nir_dir
            case ImageType.red_edge:
                return self.red_e_dir

            case _:
                raise ValueError("Invalid image type")
