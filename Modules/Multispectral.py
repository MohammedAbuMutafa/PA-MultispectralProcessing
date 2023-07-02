import rasterio
import numpy as np

class Multispectral_Processor:

    def __load_image_to_array__(self, file_name):
        
        loaded_image = rasterio.open(file_name)        
        return loaded_image.read(1).astype('float64')


    def ndvi(self, red_image_name, nir_image_name):

        nir = self.__load_image_to_array__(nir_image_name)
        red = self.__load_image_to_array__(red_image_name)

        ndvi = np.where((nir + red) == 0., 
                        0, (nir - red) / 
                        (nir + red))

        return ndvi


    def gndvi(self, nir_image_name, green_image_name):
        
        green = self.__load_image_to_array__(green_image_name)
        nir = self.__load_image_to_array__(nir_image_name)

        gndvi = np.where((nir + green) == 0., 0, 
                         (nir - green) / 
                         (nir + green))

        return gndvi
    

    def bai(self, red_image_name, nir_image_name):

        red = self.__load_image_to_array__(red_image_name)
        nir = self.__load_image_to_array__(nir_image_name)

        bai = 1 /( (np.power((0.1 - red), 2)) 
                  + np.power((0.06 - nir), 2) )
    
        return bai
    
    def savi(self, red_image_name, nir_image_name):
        
        red = self.__load_image_to_array__(red_image_name)
        nir = self.__load_image_to_array__(nir_image_name)

        tuning_param_l = 0.5

        savi = (((nir - red) / 
                (nir + red + tuning_param_l))*
                (1 + tuning_param_l))
        
        return savi
    
    def cig(self, nir_image_name, green_image_name):

        nir = self.__load_image_to_array__(nir_image_name)
        green = self.__load_image_to_array__(green_image_name)

        CIg = (nir / green) - 1

        return CIg
    
    def cire(self, nir_image_name, red_e_image_name):

        nir = self.__load_image_to_array__(nir_image_name)
        red_e = self.__load_image_to_array__(red_e_image_name)

        CIre = (nir / red_e) - 1

        return CIre
    
    def gemi(self, nir_image_name, red_image_name):

        nir = self.__load_image_to_array__(nir_image_name)
        red = self.__load_image_to_array__(red_image_name)

        nir_squared = np.power(nir, 2)
        red_squared = np.power(red, 2)

        theta = ((2 * (nir_squared - red_squared) + 1.5*nir + 0.5*red) /
                (nir + red + 0.5))
        
        gemi = (theta * (1 - 0.25 * theta) - ((red - 0.125)) /
                (1-red))
        
        return gemi
    
    def msavi2(self, nir_image_name, red_image_name):

        nir = self.__load_image_to_array__(nir_image_name)
        red = self.__load_image_to_array__(red_image_name)

        msavi2 = ((0.5 * (2 * (nir + 1)))
                    - (np.sqrt(np.power((2*nir + 1), 2)))
                    - 8*(nir - red))
        
        return msavi2
    
    def mtvi2(self, red_image_name, green_image_name, nir_image_name):
        
        red = self.__load_image_to_array__(red_image_name)
        green = self.__load_image_to_array__(green_image_name)
        nir = self.__load_image_to_array__(nir_image_name)

        mtvi2 = (1.5 * (1.2 * (nir - green) - 2.5* (red - green)) * 
                 np.sqrt(np.power((2 * nir + 1), 2) - 
                         (6 * nir - 5 * np.sqrt(red)) - 0.5))

        return mtvi2
    

    def ndre(self, nir_image_name, red_e_image_name):

        nir = self.__load_image_to_array__(nir_image_name)
        red_e = self.__load_image_to_array__(red_e_image_name)

        ndre = np.where((nir + red_e) == 0, 0,
                        (nir - red_e) / (nir + red_e))
        
        return ndre
    
    def ndwi(self, green_image_name, nir_image_name):

        green = self.__load_image_to_array__(green_image_name)
        nir = self.__load_image_to_array__(nir_image_name)

        ndwi =  np.where((green + nir) == 0, 0,
                (green - nir) / (green + nir))
        
        return ndwi
    

    def srre(self, nir_image_name, red_e_image_name):

        nir = self.__load_image_to_array__(nir_image_name)
        red_e = self.__load_image_to_array__(red_e_image_name)

        srre = nir / red_e

        return srre
    

    def rtvi_core(self, nir_image_name, green_image_name):

        nir = self.__load_image_to_array__(nir_image_name)
        green = self.__load_image_to_array__(green_image_name)

        rtvi = np.where((green + nir) == 0, 0,
                (green - nir) / (green + nir))
        
        return rtvi



