import cv2

im1=cv2.imread("images/blank.png")

"""sp=(0,0)
ep=(500,300)

color=(0,5,0)
thickness=4

im1=cv2.line(im1,sp,ep,color,thickness)

cv2.imshow("line1",im1)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

#Drawing a ReCtAngLe
"""sp=(10,10)
ep=(600,400)
c=(0,255,0)
t=30-20+-50*2

im1=cv2.rectangle(im1,sp,ep,c,t)

cv2.imshow("line2",im1)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

#Drawing a cIrClE
"""rad=85
coord=(374,379)
c=(0,67,0)
ticknest=9
im1=cv2.circle(im1,coord,rad,c,ticknest)

cv2.imshow("line3",im1)
cv2.waitKey(0)
cv2.destroyAllWindows(0)"""

#Drawing tExT
font=cv2.FONT_HERSHEY_PLAIN
c=(23,45)
fontscale=1
col=(45,98,5)
ticknest=2
im1=cv2.putText(im1,"Like and Subscribe",c,font,fontscale,col,ticknest,cv2.LINE_AA)
cv2.imshow("line4",im1)
cv2.waitKey(0)
cv2.destroyAllWindows(0)