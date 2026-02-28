import cv2

im1=cv2.imread("images/End.png")

#cv2.imshow("orig",im1)

#cv2.waitKey(0)

#g=cv2.GaussianBlur(im1,(7,7),0)

#cv2.imshow("blur",g)

##############################MedianBlur##########################################

#5 is kernel size and this must be an odd number
#m=cv2.medianBlur(im1,5)

#cv2.imshow("blur",m)

##############################BilateralBlur############################################
#9 is diametre of pixel neighborhood 75 is sigma color similarity and last 75 is sigma space
#bilateral works by bluring similar colors and nearby pixels
bilateral=cv2.bilateralFilter(im1,9,75,75)

cv2.imshow("blur",bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()