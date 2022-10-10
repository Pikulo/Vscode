'''检查python版本'''
import sys
print ("Python Version {}".format(str(sys.version).replace('\n', '')))

from tensorflow.python.client import device_lib
 
print(device_lib.list_local_devices())

import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

import time
import keras_cv
from tensorflow import keras
import matplotlib.pyplot as plt
model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)
images = model.text_to_image("photograph of an astronaut riding a horse", batch_size=3)


def plot_images(images):
    plt.figure(figsize=(20, 20))
    for i in range(len(images)):
        ax = plt.subplot(1, len(images), i + 1)
        plt.imshow(images[i])
        plt.axis("off")


plot_images(images)

