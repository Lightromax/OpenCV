import cv2

im1=cv2.imread("images/End.png")
im2=cv2.imread("images/any.png")

grey=cv2.cvtColor(im1,cv2.COLOR_BGR2GRAY)

cv2.imshow("grey",grey)

im3=cv2.imread("images/image_1.jpg")

(row,column)=im3.shape[0:2]

for i in range(row):
    for j in range(column):
        im3[i,j]=sum(im3[i,j])*0.33

cv2.waitKey(0)
cv2.imshow("grey2",im3)

cv2.waitKey(0)
cv2.destroyAllWindows()