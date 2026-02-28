import cv2
import numpy as np

image1=cv2.imread("images/image_1.jpg")
image2=cv2.imread("images/image_2.jpg")

#weightedsum=cv2.addWeighted(image1,0.5,image2,0.4,0)

#cv2.imshow("Title",weightedsum)
#################################
#sub=cv2.subtract(image1,image2)

#cv2.imshow("title",sub)

cv2.waitKey(0)
cv2.destroyAllWindows()