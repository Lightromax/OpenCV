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
#Convexity is how solid the shape is
#Inertia is the amount of elongation on the blob
para.filterByConvexity=True
para.minConvexity=0.2
para.filterByInertia=True
para.minInertiaRatio=0.01

detector=cv2.SimpleBlobDetector_create(para)
keypoints=detector.detect(im) #keypoints contains the diametre and position of the blob
blank=np.zeros((1,1))
blobs=cv2.drawKeypoints(im, keypoints, blank,(119,28,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
numberOfBlobs=len(keypoints)

font=cv2.FONT_HERSHEY_PLAIN
c=(23,45)
fontscale=1.3
col=(255,45,45)
thickness=2
im=cv2.putText(blobs,"Number of circular blobs: "+str(numberOfBlobs),(1,89),font,fontscale,col,thickness)

cv2.imshow("blurrrrrrb",blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()