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

redDirectory = os.path.join(basePath, imageDirectories["redDir"], "Train_Images")
nirDirectory = os.path.join(basePath, imageDirectories["nirDir"], "Train_Images")
greenDirectory = os.path.join(basePath, imageDirectories["greenDir"], "Train_Images")
redEdgeDirectory = os.path.join(basePath, imageDirectories["redEdgeDir"], "Train_Images")

multispectral_processor = Multispectral()

def plotResult(img, title):
    plt.imshow(img, cmap=('RdYlGn'))
    plt.colorbar()
    plt.show()    

fileBase = f"Image_001.jpg"
red_image = os.path.join(redDirectory, fileBase)
nir_image = os.path.join(nirDirectory, fileBase)

ndvi = multispectral_processor.calculate_ndvi(red_image, nir_image)
plotResult(ndvi, fileBase)

















