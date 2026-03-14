import cv2

im1=cv2.imread("images/Pris.png")

(row,column)=im1.shape[0:2]

#Step1:
    #create the rotation matrix
    
#column/2 and row/2 are to make the image rotate around the centre, 45 is the angle in which the image rotates and 1 is the scale
m=cv2.getRotationMatrix2D((column/2,row/2),45,1)
#Step2:
    #apply the rotation transformation
result=cv2.warpAffine(im1,m,(column,row))

cv2.imwrite("images/image.png",result)