from PIL import Image
img = Image.open('test.png')
img = img.resize((32,32))
img = img.convert('L')
# img.show()
import numpy as np
img_new = img.point(lambda x: 0 if x > 128 else 1)
arr = np.array(img_new)
for i in range(arr.shape[0]):
     print(arr[i])
arr_new = arr.reshape(1, -1)
print(arr_new)
