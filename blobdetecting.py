import cv2
import numpy as np

im=cv2.imread("images/blob-detect.png",0)

para=cv2.SimpleBlobDetector_Params()

#Area is the amount of space on a circle, minArea(minimum Area) is the least amount of pixels that can be considered a circle can have
#Circularity is the roundness of the circle, minCircularity is the least amount of roundness the circle can have.
para.filterByArea=True
para.minArea=100
para.filterByCircularity=True
para.minCircularity=0.9
para.filterByConvexity=True
para.minConvexity=0.2
para.filterByInertia=True
para.minInertiaRatio=0.01