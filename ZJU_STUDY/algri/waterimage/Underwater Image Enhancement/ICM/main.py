import os
import numpy as np
import cv2
import natsort
import xlwt
from global_histogram_stretching import stretching
from hsvStretching import HSVStretching
from sceneRadiance import sceneRadianceRGB


np.seterr(over='ignore')
if __name__ == '__main__':
    pass


img = cv2.imread('111.jpg')
img = stretching(img)
sceneRadiance = sceneRadianceRGB(img)
# cv2.imwrite(folder + '/OutputImages/' + Number + 'Stretched.jpg', sceneRadiance)
sceneRadiance = HSVStretching(sceneRadiance)
sceneRadiance = sceneRadianceRGB(sceneRadiance)
cv2.imwrite('111_ICM.jpg', sceneRadiance)
