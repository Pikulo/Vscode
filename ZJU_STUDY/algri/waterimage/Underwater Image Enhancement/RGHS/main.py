
# encoding=utf-8
import os
import numpy as np
import cv2
import natsort

from LabStretching import LABStretching
from color_equalisation import RGB_equalisation
from global_stretching_RGB import stretching
from relativeglobalhistogramstretching import RelativeGHstretching

np.seterr(over='ignore')
if __name__ == '__main__':
    pass


img = cv2.imread('111.jpg')
height = len(img)
width = len(img[0])
# print(img)
sceneRadiance = img
# sceneRadiance = RelativeGHstretching(sceneRadiance, height, width)

sceneRadiance = stretching(sceneRadiance)


sceneRadiance = LABStretching(sceneRadiance)

cv2.imwrite('111_RGHS.jpg', sceneRadiance)
