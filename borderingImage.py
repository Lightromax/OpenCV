import cv2

im=cv2.imread("images/image_2.jpg")

#10,10,10,10 are the border sides then comes the border type and color value
bi=cv2.copyMakeBorder(im,10,10,10,10,cv2.BORDER_CONSTANT,value=1)

br=cv2.copyMakeBorder(im,10,10,10,10,cv2.BORDER_REFLECT,value=1)

cv2.imshow("bi",bi)

cv2.imshow("br",br)

cv2.waitKey(0)
cv2.destroyAllWindows()