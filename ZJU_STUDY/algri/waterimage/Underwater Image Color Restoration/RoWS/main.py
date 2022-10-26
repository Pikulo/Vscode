import os
import numpy as np
import cv2
import natsort

from RefinedTramsmission import Refinedtransmission
from getAtomsphericLight import getAtomsphericLight
from getRGBDarkChannel import getDarkChannel
from getTM import getTransmission
from sceneRadiance import sceneRadianceRGB

np.seterr(over='ignore')
if __name__ == '__main__':
    pass




img = cv2.imread('111.jpg')
blockSize = 9

RGB_Darkchannel = getDarkChannel(img, blockSize)
AtomsphericLight = getAtomsphericLight(RGB_Darkchannel, img)
print('AtomsphericLight', AtomsphericLight)
transmission = getTransmission(img, AtomsphericLight, blockSize)
print('transmission',transmission)
print('np.mean(transmission)',np.mean(transmission))
transmission = Refinedtransmission(transmission, img)
sceneRadiance = sceneRadianceRGB(img, transmission, AtomsphericLight)
# # print('AtomsphericLight',AtomsphericLight)
#
#
#
cv2.imwrite('111_RoWS_TM.jpg', np.uint8(transmission* 255))
cv2.imwrite('111_RoWS.jpg', sceneRadiance)


