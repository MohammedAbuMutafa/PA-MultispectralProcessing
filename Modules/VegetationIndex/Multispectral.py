import numpy as np
from Helpers.ImageLoaderHelper import ImageLoaderHelper
from Enums.ImageTypeEnum import ImageType


class Multispectral:

    def __init__(self):
        self.image_loader = ImageLoaderHelper()

    def __normalize__(self, vi_array):

        normalized = (vi_array-np.min(vi_array)) / \
            (np.max(vi_array)-np.min(vi_array))
        return normalized

    def ndvi(self, fileName: str):

        nir = self.image_loader.load(fileName, ImageType.nir)
        red = self.image_loader.load(fileName, ImageType.red)

        ndvi = np.where((nir + red) == 0.,
                        0, (nir - red) /
                        (nir + red))

        normalized_ndvi = self.__normalize__(ndvi)

        return normalized_ndvi

    def gndvi(self, fileName):

        green = self.image_loader.load(fileName, ImageType.green)
        nir = self.image_loader.load(fileName, ImageType.nir)

        gndvi = np.where((nir + green) == 0., 0,
                         (nir - green) /
                         (nir + green))

        normalized_gndvi = self.__normalize__(gndvi)

        return normalized_gndvi

    def bai(self, red_image_name, nir_image_name):

        red = self.__load_image_to_array__(red_image_name)
        nir = self.__load_image_to_array__(nir_image_name)

        bai = 1 / ((np.power((0.1 - red), 2))
                   + np.power((0.06 - nir), 2))

        normalized_bai = self.__normalize__(bai)

        return normalized_bai

    def savi(self, red_image_name, nir_image_name, tuning_param_l=0.5):

        red = self.__load_image_to_array__(red_image_name)
        nir = self.__load_image_to_array__(nir_image_name)

        savi = (((nir - red) /
                (nir + red + tuning_param_l)) *
                (1 + tuning_param_l))

        normalized_savi = self.__normalize__(savi)

        return normalized_savi

    def cig(self, nir_image_name, green_image_name):

        nir = self.__load_image_to_array__(nir_image_name)
        green = self.__load_image_to_array__(green_image_name)

        CIg = (nir / green) - 1

        normalized_cig = self.__normalize__(CIg)
        return normalized_cig

    def cire(self, nir_image_name, red_e_image_name):

        nir = self.__load_image_to_array__(nir_image_name)
        red_e = self.__load_image_to_array__(red_e_image_name)

        CIre = (nir / red_e) - 1

        normalized_cire = self.__normalize__(CIre)
        return normalized_cire

    def gemi(self, nir_image_name, red_image_name):

        nir = self.__load_image_to_array__(nir_image_name)
        red = self.__load_image_to_array__(red_image_name)

        nir_squared = np.power(nir, 2)
        red_squared = np.power(red, 2)

        theta = ((2 * (nir_squared - red_squared) + 1.5*nir + 0.5*red) /
                 (nir + red + 0.5))

        gemi = (theta * (1 - 0.25 * theta) - ((red - 0.125)) /
                (1-red))

        normalized_gemi = self.__normalize__(gemi)

        return normalized_gemi

    def msavi2(self, nir_image_name, red_image_name):

        nir = self.__load_image_to_array__(nir_image_name)
        red = self.__load_image_to_array__(red_image_name)

        msavi2 = ((0.5 * (2 * (nir + 1)))
                  - (np.sqrt(np.power((2*nir + 1), 2)))
                  - 8*(nir - red))

        normalized_msavi2 = self.__normalize__(msavi2)
        return normalized_msavi2

    def mtvi2(self, red_image_name, green_image_name, nir_image_name):

        red = self.__load_image_to_array__(red_image_name)
        green = self.__load_image_to_array__(green_image_name)
        nir = self.__load_image_to_array__(nir_image_name)

        mtvi2 = (1.5 * (1.2 * (nir - green) - 2.5 * (red - green)) *
                 np.sqrt(np.power((2 * nir + 1), 2) -
                         (6 * nir - 5 * np.sqrt(red)) - 0.5))

        normalized_mtvi2 = self.__normalize__(mtvi2)

        return normalized_mtvi2

    def ndre(self, nir_image_name, red_e_image_name):

        nir = self.__load_image_to_array__(nir_image_name)
        red_e = self.__load_image_to_array__(red_e_image_name)

        ndre = np.where((nir + red_e) == 0, 0,
                        (nir - red_e) / (nir + red_e))

        normalized_ndre = self.__normalize__(ndre)

        return normalized_ndre

    def ndwi(self, green_image_name, nir_image_name):

        green = self.__load_image_to_array__(green_image_name)
        nir = self.__load_image_to_array__(nir_image_name)

        ndwi = np.where((green + nir) == 0, 0,
                        (green - nir) / (green + nir))

        normalized_ndwi = self.__normalize__(ndwi)
        return normalized_ndwi

    def srre(self, nir_image_name, red_e_image_name):

        nir = self.__load_image_to_array__(nir_image_name)
        red_e = self.__load_image_to_array__(red_e_image_name)

        srre = nir / red_e

        normalized_srre = self.__normalize__(srre)

        return normalized_srre

    def rtvi_core(self, nir_image_name, green_image_name):

        nir = self.__load_image_to_array__(nir_image_name)
        green = self.__load_image_to_array__(green_image_name)

        rtvi = np.where((green + nir) == 0, 0,
                        (green - nir) / (green + nir))

        normalized_rtvi = self.__normalize__(rtvi)

        return normalized_rtvi
