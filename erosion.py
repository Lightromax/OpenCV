import cv2
import numpy as np

im1=cv2.imread("images/Pris.png",1)

kernel=np.ones((5,5),np.uint8)

image=cv2.erode(im1,kernel)

cv2.imshow("title",image)

cv2.waitKey(0)
cv2.destroyAllWindows()