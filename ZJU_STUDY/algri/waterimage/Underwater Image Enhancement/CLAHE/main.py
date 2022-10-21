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
# folder = "C:/Users/Administrator/Desktop/UnderwaterImageEnhancement/HE"
# folder = "E:/Microsoft Visual Studio Code/MY-Github-Projects/git-setting/Vscode/ZJU_STUDY/模型算法/水下图像复原处理/CLAHE"
# folder = "C:/Users/Administrator/Desktop/Databases/Dataset"

# path = folder + "/InputImages"
# files = os.listdir(path)
# print(files)
# files =  natsort.natsorted(files)

# for i in range(len(files)):
#     file = files[i]
#     filepath = path + "/" + file
#     prefix = file.split('.')[0]
#     if os.path.isfile(filepath):
#         print('********    file   ********',file)
#         # img = cv2.imread('InputImages/' + file)
#         print(folder + '/InputImages/' + file)
#         img = cv2.imread(folder + '/InputImages/' + file)
#         print(img)
#         sceneRadiance = RecoverCLAHE(img)
#         # cv2.imwrite('OutputImages/' + prefix + '_CLAHE.jpg', sceneRadiance)
#         cv2.imwrite('Temps/' + prefix + '_CLAHE.jpg', sceneRadiance)

img = cv2.imread('u=299608326,350975549&fm=193.jpg')
print(img)
sceneRadiance = RecoverCLAHE(img)
# cv2.imwrite('OutputImages/' + prefix + '_CLAHE.jpg', sceneRadiance)
cv2.imwrite('test1.jpg', sceneRadiance)