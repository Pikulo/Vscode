import os
import numpy as np
import cv2
import natsort


from DetermineDepth import determineDepth
from getAtomsphericLight import getAtomsphericLight
from getRefinedTramsmission import Refinedtransmission
from getScatteringRate import ScatteringRateMap
from getSceneRadiance import SceneRadiance
from getTransmissionGB import TransmissionGB
from getTransmissionR import TransmissionR

np.seterr(over='ignore')
if __name__ == '__main__':
    pass



img = cv2.imread('111.jpg')
blockSize = 9
largestDiff = determineDepth(img, blockSize)
AtomsphericLight = getAtomsphericLight(largestDiff, img)
print('AtomsphericLight',AtomsphericLight)
sactterRate = ScatteringRateMap(img, AtomsphericLight, blockSize)
print('sactterRate',sactterRate)
transmissionGB = TransmissionGB(sactterRate)
transmissionR = TransmissionR(transmissionGB, img, blockSize)
transmissionGB, transmissionR = Refinedtransmission(transmissionGB, transmissionR, img)
sceneRadiance = SceneRadiance(img, transmissionGB, transmissionR, sactterRate, AtomsphericLight)

cv2.imwrite('111_NewOpticalModel_TM.jpg', np.uint8(transmissionR * 255))
# cv2.imwrite('OutputImages/' + prefix + '_NewOpticalModel_TM_GB.jpg', np.uint8(transmissionGB * 255))
cv2.imwrite('111_NewOpticalModel.jpg', sceneRadiance)



# cv2.imwrite('OutputImages/' + prefix + '_MIP_TM.jpg', np.uint8(transmission * 255))
# cv2.imwrite('OutputImages/' + prefix + '_MIP.jpg', sceneRadiance)