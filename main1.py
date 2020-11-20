import re
import os
import cv2
import numpy as np
from os.path import isfile, join
import matplotlib.pyplot as plt


# empty list to store the frames
col_images = []

vidObj = cv2.VideoCapture("assets/footage.mp4") 

# checks whether frames were extracted 
success = 1
  
while success:

    success, image = vidObj.read() 
    col_images.append(image)


# kernel for image dilation
kernel = np.ones((4, 4), np.uint8)

frame_array = []

for i in range(len(col_images)-1):

    # frame differencing
    grayA = cv2.cvtColor(col_images[i], cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(col_images[i+1], cv2.COLOR_BGR2GRAY)
    diff_image = cv2.absdiff(grayB, grayA)

    # image thresholding
    ret, thresh = cv2.threshold(diff_image, 70, 255, cv2.THRESH_BINARY)

    # image dilation
    dilated = cv2.dilate(thresh, kernel, iterations=1)

    # find contours
    contours, hierarchy = cv2.findContours(
        dilated.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # add contours to original frames
    dmy = col_images[i].copy()
    cv2.drawContours(dmy, contours, -1, (127, 200, 0), 1)

    height, width, layers = dmy.shape
    size = (width,height)

    frame_array.append(dmy)

# specify video name
pathOut = 'vehicle_detection.mp4'

# specify frames per second
fps = 14.0

out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

for i in range(len(frame_array)):
     out.write(frame_array[i])

out.release()

