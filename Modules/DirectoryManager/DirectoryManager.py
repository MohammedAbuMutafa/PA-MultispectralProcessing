import os
import logging
from datetime import datetime


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
                self.base_input_dir, self.image_folders[key], "Train_Images")

    def __init_output_dir__(self):
        self.output_dir = {}
        self.base_output_dir = os.getenv("OUTPUT_BASE_PATH")

        if (os.path.exists(self.base_output_dir) == False):
            self.logger.info("Creating Main output directory")
            os.mkdir(self.base_output_dir)
        else:
            self.logger.info("Main output directory exists")

        self.__create_session_dirs__()

    def get_output_dirs(self) -> dict():
        return self.output_dir

    def get_input_dirs(self) -> dict():
        return self.input_dir

    def __create_session_dirs__(self):
        session_dir = os.getenv('SESSION_KEY')
        now = datetime.now()
        date = now.strftime("%d%m%Y%H%M%S")
        file_name = (str)(session_dir) + date
        output_dir = os.path.join(
            self.base_output_dir, file_name)

        os.mkdir(output_dir)
        self.logger.info(f"Creating output dir: {output_dir}")

        processed = os.path.join(output_dir, "Processed")
        self.output_dir["PROCESSED"] = processed
        os.mkdir(processed)

        classified = os.path.join(output_dir, "Classified")
        self.output_dir["CLASSIFIED"] = classified
        os.mkdir(classified)
