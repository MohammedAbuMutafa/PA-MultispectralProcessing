import os
import dotenv
import rasterio
from Enums.ImageTypeEnum import ImageType
import logging


class ImageLoaderHelper():

    def __init__(self):
        dotenv.load_dotenv()
        self.__init_directories__()
        logging.getLogger("rasterio").setLevel(logging.WARNING)

    def __init_directories__(self):
        self.base_path = os.getenv('DATA_BASE_PATH')
        self.green_dir = os.getenv('GREEN_DIR')
        self.nir_dir = os.getenv('NIR_DIR')
        self.red_dir = os.getenv('RED_DIR')
        self.red_e_dir = os.getenv('RED_EDGE_DIR')

    def load(self, file_name: str, image_type: ImageType):

        try:
            file = os.path.join(
                self.base_path, self.__get_image_type__(image_type), file_name)
            image = rasterio.open(file)
            return image.read(1).astype('float64')
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
