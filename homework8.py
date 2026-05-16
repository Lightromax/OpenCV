import cv2
import numpy as np

im=cv2.imread("images/coins2.png",0)

para=cv2.SimpleBlobDetector_Params()

para.filterByArea=True
para.minArea=10000
para.maxArea=80000
para.filterByConvexity=True
para.minConvexity=0.8
para.filterByCircularity=True
para.minCircularity=0.3
para.filterByInertia=True
para.minInertiaRatio=0.5

resize=cv2.resize(im,(1000,900))

dectect=cv2.SimpleBlobDetector_create(para)
keypoints=dectect.detect(resize)
blank=np.zeros((1,1))
blob=cv2.drawKeypoints(resize,keypoints,blank,(119,28,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
numberOfBlobs=len(keypoints)

font=cv2.FONT_HERSHEY_PLAIN
fontScale=2
color=(34,45,43)
ticknest=2

cv2.putText(blob,"NumberOfCoins"+str(numberOfBlobs),(1,89),font,fontScale,color,ticknest)

cv2.imshow("coins detected",blob)
cv2.waitKey(0)
cv2.destroyAllWindows()