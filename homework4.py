import cv2

im=cv2.imread("images/Pris.png")

startp=(0,0)
ep=(500,300)
color=(0,5,0)
t=3
bradius=67
coord=(344,369)

im=cv2.line(im,startp,ep,color,t)

cv2.imshow("line1",im)
cv2.waitKey(0)
im2=cv2.rectangle(im,startp,ep,color,t)
cv2.imshow("line2",im2)
cv2.waitKey(0)
im3=cv2.circle(im,coord,bradius,color,t)
cv2.imshow("line3",im3)
cv2.waitKey(0)
font=cv2.FONT_HERSHEY_COMPLEX
c2=(23,45)
fontscale=2
col=(78,38,85)
ticknest=2
im1=cv2.putText(im,"I did it!!!",c2,font,fontscale,col,t,cv2.LINE_AA)
cv2.imshow("line4",im1)
cv2.waitKey(0)
cv2.destroyAllWindows()