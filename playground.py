from Modules.Multispectral import Multispectral
import os
import matplotlib.pyplot as plt
from dotenv import load_dotenv

class Playground():

    def __init__(self):

        load_dotenv()
        self.__init_paths__()

    def __init_paths__(self):

        dataDir = os.getenv('DATA_BASE_PATH')
        redDir = os.getenv("RED_DIR")
        nirDir = os.getenv("NIR_DIR")
        greenDir = os.getenv("GREEN_DIR")
        redEdgeDir = os.getenv("RED_EDGE_DIR")

        self.redDirectory = os.path.join(dataDir, redDir, "Train_Images")
        self.nirDirectory = os.path.join(dataDir, nirDir, "Train_Images")
        self.greenDirectory = os.path.join(dataDir, greenDir, "Train_Images")
        self.redEdgeDirectory = os.path.join(dataDir, redEdgeDir, "Train_Images")

    def plotResult(self, img):
        plt.imshow(img, cmap=('RdYlGn'))
        plt.colorbar()
        plt.show()    


main = Playground()
multispectral_processor = Multispectral()

fileBase = f"Image_001.jpg"
red_image = os.path.join(main.redDirectory, fileBase)
nir_image = os.path.join(main.nirDirectory, fileBase)

savi = multispectral_processor.calculate_savi(red_image, nir_image)
main.plotResult(savi)

ndvi = multispectral_processor.calc
















