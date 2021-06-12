import cv2
import numpy as np
from PIL import Image, ImageDraw


class TransformImage(object):

    def __init__(self, debug=False):
        self.debug = debug
    
    def preprocess(self, image):
        image = image.copy()
        #image = cv2.bitwise_not(image)
        # Convert the BRG image to RGB
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        R,G,B = cv2.split(img)
        R[R > 200] = 255
        G[G > 200] = 255
        B[B > 200] = 255
        R[R < 100] = 0
        G[G < 100] = 0
        B[B < 100] = 0
        image_RGB = cv2.merge([R,G, B])
        image = cv2.cvtColor(image_RGB, cv2.COLOR_RGB2BGR)
        # Convert the RGB image to HSV

        #img = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        #hue,sat,val = cv2.split(img)
        #sat[sat > 115] = 255
        #val[val > 115] = 115
        #image_HSV = cv2.merge([hue,sat, val])
        #image = cv2.cvtColor(image_HSV, cv2.COLOR_HSV2BGR)

        height, _, _ = image.shape
        image[  :int(height/4)  ,  :  ,  :  ] = 0
 
        return image

    def run(self, img_arr, debug=False):
        if img_arr is None:
            return img_arr
        img = self.preprocess(img_arr)

        return img
