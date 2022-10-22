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

img = cv2.imread('blue_07.jpg')
sceneRadiance = RecoverCLAHE(img)
cv2.imwrite('blue_07_CLAHE.jpg', sceneRadiance)


