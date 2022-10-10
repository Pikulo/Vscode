import os
import pandas as pd
 
path = r'D:\手机上的照片&视频\kiddy&kiddo\test_2022'
files= os.listdir(path)
print(files)
os.chdir(path)
for i in files:
    os.rename(i,'临海_2022_10_05')
