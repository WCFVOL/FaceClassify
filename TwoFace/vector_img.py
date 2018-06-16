import random

import cv2
import numpy as np


def vector_img(img, image_size):
    arrs = []
    image_vector_len = np.prod(image_size)
    #cv2.imwrite(str(random.randint(0, 9)) + '11.jpg', img)
    arr_img = np.asarray(img, dtype='float64')
    arr_img = arr_img.transpose(2, 0, 1)
    arr_img = arr_img.reshape((image_vector_len,))
    arrs.append(arr_img)
    return np.asarray(arrs, dtype='float64')
