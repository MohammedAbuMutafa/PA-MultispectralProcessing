from Modules.Multispectral import Multispectral
import os
import matplotlib.pyplot as plt


dataDir = os.path.join("Data", "Spectral_Images")
basePath = os.path.join(os.getcwd(), dataDir)

imageDirectories = {    
    "greenDir": "Green_Channel",
    "nirDir": "Near_Infrared_Channel",
    "redDir": "Red_Channel",
    "redEdgeDir": "Red_Edge_Channel",
}

redDirectory = os.path.join(basePath, imageDirectories["redDir"])
nirDirectory = os.path.join(basePath, imageDirectories["nirDir"])
greenDirectory = os.path.join(basePath, imageDirectories["greenDir"])
redEdgeDirectory = os.path.join(basePath, imageDirectories["redEdgeDir"])

multispectral_processor = Multispectral()

def plotResult(img):
    plt.imshow(img, cmap=('RdYlGn'))
    plt.colorbar()
    plt.show()

for i in range(1,9):

    fileBase = f"Image_00{i}.jpg"
    red_image = os.path.join(redDirectory, fileBase)
    nir_image = os.path.join(nirDirectory, fileBase)

    ndvi = multispectral_processor.processNdvi(red_image, nir_image)
    plotResult(ndvi)


