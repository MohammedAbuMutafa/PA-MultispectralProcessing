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

    def ndvi(self, filename: str):

        nir = self.image_loader.load(filename, ImageType.nir)
        red = self.image_loader.load(filename, ImageType.red)

        ndvi = np.where((nir + red) == 0.,
                        0, (nir - red) /
                        (nir + red))

        # normalized_ndvi = self.__normalize__(ndvi)

        return ndvi

    def gndvi(self, filename):

        green = self.image_loader.load(filename, ImageType.green)
        nir = self.image_loader.load(filename, ImageType.nir)

        gndvi = np.where((nir + green) == 0., 0,
                         (nir - green) /
                         (nir + green))

        # normalized_gndvi = self.__normalize__(gndvi)

        return gndvi

    def bai(self, filename):

        red = self.image_loader.load(filename, ImageType.red)
        nir = self.image_loader.load(filename, ImageType.nir)

        bai = 1 / ((np.power((0.1 - red), 2))
                   + np.power((0.06 - nir), 2))

        # normalized_bai = self.__normalize__(bai)

        return bai

    def savi(self, filename, tuning_param_l=0.5):

        red = self.image_loader.load(filename, ImageType.red)
        nir = self.image_loader.load(filename, ImageType.nir)

        savi = (((nir - red) /
                (nir + red + tuning_param_l)) *
                (1 + tuning_param_l))

        # normalized_savi = self.__normalize__(savi)

        return savi

    def cig(self, filename):

        nir = self.image_loader.load(filename, ImageType.nir)
        green = self.image_loader.load(filename, ImageType.green)

        CIg = (nir / green) - 1

        # normalized_cig = self.__normalize__(CIg)
        return CIg

    def cire(self, filename):

        nir = self.image_loader.load(filename, ImageType.nir)
        red_e = self.image_loader.load(filename, ImageType.red_edge)

        CIre = (nir / red_e) - 1

        # normalized_cire = self.__normalize__(CIre)
        return CIre

    def gemi(self, filename):

        nir = self.image_loader.load(filename, ImageType.nir)
        red = self.image_loader.load(filename, ImageType.red)

        nir_squared = np.power(nir, 2)
        red_squared = np.power(red, 2)

        theta = ((2 * (nir_squared - red_squared) + 1.5*nir + 0.5*red) /
                 (nir + red + 0.5))

        gemi = (theta * (1 - 0.25 * theta) - ((red - 0.125)) /
                (1-red))

        # normalized_gemi = self.__normalize__(gemi)

        return gemi

    def msavi2(self, filename):

        nir = self.image_loader.load(filename, ImageType.nir)
        red = self.image_loader.load(filename, ImageType.red)

        msavi2 = ((0.5 * (2 * (nir + 1)))
                  - (np.sqrt(np.power((2*nir + 1), 2)))
                  - 8*(nir - red))

        # normalized_msavi2 = self.__normalize__(msavi2)
        return msavi2

    def mtvi2(self, filename):

        red = self.image_loader.load(filename, ImageType.red)
        green = self.image_loader.load(filename, ImageType.green)
        nir = self.image_loader.load(filename, ImageType.nir)

        mtvi2 = (1.5 * (1.2 * (nir - green) - 2.5 * (red - green)) *
                 np.sqrt(np.power((2 * nir + 1), 2) -
                         (6 * nir - 5 * np.sqrt(red)) - 0.5))

        # normalized_mtvi2 = self.__normalize__(mtvi2)

        return mtvi2

    def ndre(self, filename):

        nir = self.image_loader.load(filename, ImageType.nir)
        red_e = self.image_loader.load(filename, ImageType.red_edge)

        ndre = np.where((nir + red_e) == 0, 0,
                        (nir - red_e) / (nir + red_e))

        # normalized_ndre = self.__normalize__(ndre)

        return ndre

    def ndwi(self, filename):

        green = self.image_loader.load(filename, ImageType.green)
        nir = self.image_loader.load(filename, ImageType.nir)

        ndwi = np.where((green + nir) == 0, 0,
                        (green - nir) / (green + nir))

        # normalized_ndwi = self.__normalize__(ndwi)
        return ndwi

    def srre(self, filename):

        nir = self.image_loader.load(filename, ImageType.nir)
        red_e = self.image_loader.load(filename, ImageType.red_edge)

        srre = nir / red_e

        # normalized_srre = self.__normalize__(srre)

        return srre

    def rtvi_core(self, filename):

        nir = self.image_loader.load(filename, ImageType.nir)
        green = self.image_loader.load(filename, ImageType.green)

        rtvi = np.where((green + nir) == 0, 0,
                        (green - nir) / (green + nir))

        # normalized_rtvi = self.__normalize__(rtvi)

        return rtvi
