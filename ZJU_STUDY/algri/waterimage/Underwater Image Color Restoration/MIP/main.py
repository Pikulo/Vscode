import os
import numpy as np
import cv2
import natsort

from BL import getAtomsphericLight
from EstimateDepth import DepthMap
from getRefinedTramsmission import Refinedtransmission
from TM import getTransmission
from sceneRadiance import sceneRadianceRGB

np.seterr(over='ignore')
if __name__ == '__main__':
    pass

# folder = "C:/Users/Administrator/Desktop/UnderwaterImageEnhancement/Physical/MIP"

img = cv2.imread('111.jpg')
blockSize = 9
largestDiff = DepthMap(img, blockSize)
transmission = getTransmission(largestDiff)
transmission = Refinedtransmission(transmission,img)
AtomsphericLight = getAtomsphericLight(transmission, img)
sceneRadiance = sceneRadianceRGB(img, transmission, AtomsphericLight)

# cv2.imwrite('OutputImages/' + prefix + '_CLAHE.jpg', sceneRadiance)
cv2.imwrite('111_MIP_TM.jpg', np.uint8(transmission * 255))
cv2.imwrite('111_MIP.jpg', sceneRadiance)