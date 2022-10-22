
import os
import numpy as np
import cv2
import natsort
import xlwt
from skimage import exposure

from sceneRadianceGC import RecoverGC

np.seterr(over='ignore')
if __name__ == '__main__':
    pass

img = cv2.imread('111.jpg')
sceneRadiance = RecoverGC(img)
print('sceneRadiance',sceneRadiance)
cv2.imwrite('111_GC.jpg', sceneRadiance)
