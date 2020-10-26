import numpy as np
import cv2
from mss.linux import MSS as mss
from PIL import Image
import time
import pyautogui as pg
import imutils
import mss
import numpy
import pyautogui


def process_image(original_image):
    processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    processed_image = cv2.Canny(processed_image, threshold1=200, threshold2=300)
    return processed_image


img = cv2.imread('sss.png')
process_img = process_image(img)
print(process_img)
mean = np.mean(process_img)
print('mean =', mean)