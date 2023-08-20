from Helpers.ImageFormatHelper import ImageFormatHelper


class Classifier():

    def __init__(self) -> None:
        self.image_format_helper = ImageFormatHelper()
        pass

    def classify_ndvi(self, image_path):
        
