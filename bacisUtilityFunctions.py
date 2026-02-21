import cv2

image1=cv2.imread("any.png")
image2=cv2.imread("End.png")

weightedsum=cv2.addWeighted(image1,0.5,image2,0.4,0)

cv2.imshow("Title",weightedsum)

cv2.waitKey(0)
cv2.destroyAllWindows()