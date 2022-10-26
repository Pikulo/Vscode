
import os
import numpy as np
import cv2
import natsort
import xlwt
from skimage import exposure

from sceneRadianceCLAHE import RecoverCLAHE
from sceneRadianceHE import RecoverHE

np.seterr(over='ignore')
if __name__ == '__main__':
    pass

img = cv2.imread('111_UCM.jpg')
sceneRadiance = RecoverHE(img)
cv2.imwrite('111_UCM_HE.jpg', sceneRadiance)
