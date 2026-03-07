import cv2
import numpy as np

im1=cv2.imread("images/any.png")
im2=cv2.imread("images/End.png")
im3=cv2.imread("images/image_1.jpg")
im4=cv2.imread("images/image_2.jpg")

kernel=np.ones((5,5),np.uint8)
added=cv2.addWeighted(im3,0.5,im4,0.4,1)
subed=cv2.subtract(im3,im4)
res=cv2.resize(im2,(500,500))
eroded=cv2.erode(im1,kernel)
blur=cv2.GaussianBlur(im3,(7,7),0)
bord=cv2.copyMakeBorder(im1,10,10,10,10,cv2.BORDER_CONSTANT)

cv2.imshow("eroded",eroded)
cv2.waitKey(0)
cv2.imshow("add",added)
cv2.waitKey(0)
cv2.imshow("sub",subed)
cv2.waitKey(0)
cv2.imshow("res",res)
cv2.waitKey(0)
cv2.imshow("blur",blur)
cv2.waitKey(0)
cv2.imshow("bord",bord)
cv2.waitKey(0)
cv2.destroyAllWindows()