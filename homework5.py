import cv2
import numpy as np

im=cv2.imread("images/icu.png",cv2.IMREAD_COLOR)
grey=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
blur=cv2.blur(grey,(3,3))

detectCircles=cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=1,maxRadius=40)

if detectCircles is not None:
    detectCircle=np.uint16(np.around(detectCircles))
    for point in detectCircle[0,:]:
        a,b,r=point[0],point[1],point[2]
        cv2.circle(im,(a,b),r,(0,255,0),2)
        cv2.circle(im,(a,b),1,(0,0,255),3)
        cv2.imshow("detectedCircles",im)
        cv2.waitKey(0)
cv2.destroyAllWindows()