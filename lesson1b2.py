import cv2

img=cv2.imread("images/Pris.png")
cv2.imshow("Pris",img)
while True:
    key=cv2.waitKey(0)
    if key == ord("s"):
        cv2.imwrite("images/any.png",img)
        print("image saved")
    elif key == ord("q"):
        break
cv2.destroyAllWindows()