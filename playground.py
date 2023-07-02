from Modules.Multispectral import Multispectral_Processor
import os
import matplotlib.pyplot as plt
from dotenv import load_dotenv

class Playground():

    def __init__(self):

        load_dotenv()
        self.__init_paths__()

    def __init_paths__(self):

        self.__init_input_paths__()
        self.__init_output_paths__()

    def __init_input_paths__(self):        

        self.redDirectory = os.path.join(os.getenv('DATA_BASE_PATH'), os.getenv("RED_DIR"), "Train_Images")
        self.nirDirectory = os.path.join(os.getenv('DATA_BASE_PATH'), os.getenv("NIR_DIR"), "Train_Images")
        self.greenDirectory = os.path.join(os.getenv('DATA_BASE_PATH'), os.getenv("GREEN_DIR"), "Train_Images")
        self.redEdgeDirectory = os.path.join(os.getenv('DATA_BASE_PATH'), os.getenv("RED_EDGE_DIR"), "Train_Images")

    def __init_output_paths__(self):
        
        output_base = os.getenv('OUTPUT_BASE_PATH')

        if (os.path.exists(output_base) != True):
            os.mkdir(output_base)
        
    def plotResult(self, img):
        plt.imshow(img, cmap=('RdYlGn'))
        plt.colorbar()
        plt.show()    


main = Playground()
multispectral_processor = Multispectral_Processor()

fileBase = f"Image_001.jpg"
red_image = os.path.join(main.redDirectory, fileBase)
nir_image = os.path.join(main.nirDirectory, fileBase)

ndvi = multispectral_processor.ndvi(red_image, nir_image)
main.plotResult(ndvi)















