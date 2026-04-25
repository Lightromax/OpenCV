import cv2
import numpy as np

im=cv2.imread("images/testCircles.png",0)

para=cv2.SimpleBlobDetector_Params()

para.filterByArea=True
para.minArea=30
para.maxArea=2000000000000000
para.filterByCircularity=True
para.minCircularity=0.7
para.filterByConvexity=True
para.minConvexity=0.8
para.filterByInertia=True
para.minInertiaRatio=0.5

detector=cv2.SimpleBlobDetector_create(para)
keypoints=detector.detect(im)
blank=np.zeros((1,1))
blobs=cv2.drawKeypoints(im, keypoints, blank,(119,28,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
numberOfBlobs=len(keypoints)

font=cv2.FONT_HERSHEY_PLAIN
c=(23,45)
fontscale=1.3
col=(255,45,45)
thickness=2
im=cv2.putText(blobs,"Number of circular faces: "+str(numberOfBlobs),(1,89),font,fontscale,col,thickness)

cv2.imshow("work",blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()