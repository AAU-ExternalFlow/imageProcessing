import os
import cv2
from PIL import Image

def gaussian_blur(image, value):
    return cv2.GaussianBlur(image, (value, value), 0)

def canny(image, min_value, max_value):
    return cv2.Canny(image, min_value, max_value)

def bitwise_not(image):
    return cv2.bitwise_not(image)
