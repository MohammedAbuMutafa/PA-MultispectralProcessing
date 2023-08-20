from Enums.MultiSpectralEnum import MultiSpectralEnum
from Modules.VegetationIndex.Multispectral import Multispectral


class MultispectralFactory():
    def __init__(self) -> None:
        self.multispectral = Multispectral()

    def process(self, image, type: MultiSpectralEnum):
        match type:
            case MultiSpectralEnum.ndvi:
                return self.multispectral.ndvi(image)
            case MultiSpectralEnum.gndvi:
                return self.multispectral.gndvi(image)
            case MultiSpectralEnum.bai:
                return self.multispectral.bai(image)
            case MultiSpectralEnum.savi:
                return self.multispectral.savi(image)
            case MultiSpectralEnum.cig:
                return self.multispectral.cig(image)
            case MultiSpectralEnum.cire:
                return self.multispectral.cire(image)
            case MultiSpectralEnum.gemi:
                return self.multispectral.gemi(image)
            case MultiSpectralEnum.msavi2:
                return self.multispectral.msavi2(image)
            case MultiSpectralEnum.mtvi2:
                return self.multispectral.mtvi2(image)
            case MultiSpectralEnum.ndre:
                return self.multispectral.ndre(image)
            case MultiSpectralEnum.ndwi:
                return self.multispectral.ndwi(image)
            case MultiSpectralEnum.srre:
                return self.multispectral.srre(image)
            case MultiSpectralEnum.rtvi_core:
                return self.multispectral.rtvi_core(image)

            case _:
                raise ValueError("Invalid multispectral index")
