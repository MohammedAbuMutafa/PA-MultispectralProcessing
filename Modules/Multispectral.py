import rasterio
import numpy as np

class Multispectral:

    def __load_image__(self, file_name):
        
        loaded_image = rasterio.open(file_name)        
        return loaded_image.read(1).astype('float64')


    def calculate_ndvi(self, red_image_name, nir_image_name):

        nir_image = self.__load_image__(nir_image_name)
        red_image = self.__load_image__(red_image_name)

        ndvi = np.where((nir_image + red_image) == 0., 
                        0, (nir_image - red_image) / 
                        (nir_image + red_image))

        return ndvi


    def calculate_gndvi(self, nir_image_name, green_image_name):
        
        green_image = self.__load_image__(green_image_name)
        nir_image = self.__load_image__(nir_image_name)

        gndvi = np.where((nir_image + green_image) == 0., 0, 
                         (nir_image - green_image) / 
                         (nir_image + green_image))

        return gndvi
    

    def calculate_bai(self, red_image_name, nir_image_name):

        red_image = self.__load_image__(red_image_name)
        nir_image = self.__load_image__(nir_image_name)

        bai = 1 /( (np.power((0.1 - red_image), 2)) 
                  + np.power((0.06 - nir_image), 2) )
    
        return bai
    
    def calculate_savi(self, red_image_name, nir_image_name):
        return 0
        