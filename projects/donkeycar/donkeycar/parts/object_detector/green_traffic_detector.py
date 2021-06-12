import numpy as np
import cv2
import time
import random
import collections
import os
import urllib.request
 
class GreenTrafficDetector(object):
 
    def convertImageArrayToPILImage(self, img_arr):
        img = Image.fromarray(img_arr.astype('uint8'), 'RGB')
 
        return img
 
    '''
    Retourne si le feu vert a été detecté ou non
    '''
    def detect_green_traffic(self, img_arr):
        hsv = cv2.cvtColor(img_arr, cv2.COLOR_BGR2HSV)
 
        lower_green = np.array([40,50,50])
        upper_green = np.array([80,255,255])
 
        mask = cv2.inRange(hsv, lower_green, upper_green)
        res = cv2.bitwise_and(img_arr, img_arr, mask = mask)
 
        grey = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
 
        # applying gaussian blur
        value = (35, 35)
        blurred = cv2.GaussianBlur(grey, value, 0)
 
        _, thresh1 = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        cnt1 = min(contours, key = lambda x: cv2.contourArea(x))
        
        area = cv2.contourArea(cnt1, True)
        print("Find : ", area > 0)
        return area > 0
    
    def run(self, img_arr, debug=False):
        if img_arr is None:
            return img_arr
 
        # Detect traffic light object
        return self.detect_green_traffic(img_arr)    