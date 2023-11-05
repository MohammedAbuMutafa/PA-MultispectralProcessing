import os
import logging
from datetime import datetime
from Enums.MultiSpectralEnum import MultiSpectralEnum


class DirectoryManager():

    def __init__(self) -> None:

        self.logger = logging.getLogger(__name__)
        self.__init_directories__()

    def __init_directories__(self):

        self.image_folders = {
            "RED": os.getenv("RED_DIR"),
            "GREEN": os.getenv("GREEN_DIR"),
            "NIR": os.getenv("NIR_DIR"),
            "RED_EDGE": os.getenv("RED_EDGE_DIR")
        }

        self.__init_output_dir__()
        self.__init_input_dir__()

    def __init_input_dir__(self):
        self.input_dir = {}
        self.base_input_dir = os.getenv("DATA_DIR")

        for key in self.image_folders:
            self.input_dir[key] = os.path.join(
                self.base_input_dir, self.image_folders[key])

    def __init_output_dir__(self):
        self.output_dir = {}
        self.base_output_dir = os.getenv("OUTPUT_BASE_PATH")

        if (os.path.exists(self.base_output_dir) == False):
            self.logger.info("Creating Main output directory")
            os.mkdir(self.base_output_dir)
        else:
            self.logger.info("Main output directory exists")

    def get_output_dirs(self) -> dict():
        return self.output_dir

    def get_input_dirs(self) -> dict():
        return self.input_dir

    def create_session_dirs(self):
        self.__create_main_dir__()
        self.__create_sub_dirs__()

    def __create_main_dir__(self):
        self.session_dir = os.getenv('SESSION_KEY')
        now = datetime.now()
        date = now.strftime("%d_%m_%Y-%H_%M_%S")
        session_name = self.session_dir + '-' + date
        self.session_dir = os.path.join(
            self.base_output_dir, session_name)

        if (os.path.exists(self.session_dir) == False):
            os.mkdir(self.session_dir)
            self.logger.info(f"Creating output dir: {self.session_dir}")

    def __create_sub_dirs__(self):
        for dir in MultiSpectralEnum:
            os.makedirs(os.path.join(self.session_dir, dir.name, "numpy"))
            os.makedirs(os.path.join(
                self.session_dir, dir.name, "images"))
            debug_mode = os.getenv("DEBUG_MODE")
            if (debug_mode == "TRUE"):
                os.makedirs(os.path.join(
                    self.session_dir, dir.name, "debug"))
