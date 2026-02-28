import cv2

im1=cv2.imread("images/image_1.jpg",1)

cv2.imshow("Title",im1)
#500 is width 200 is height
resized=cv2.resize(im1,(500,200))

cv2.imshow("Title1",resized)

cv2.waitKey(0)
cv2.destroyAllWindows()