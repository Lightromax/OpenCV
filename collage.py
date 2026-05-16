import cv2
import os
from PIL import Image
#PIL stands for Pillow Image Library. For Loading pictures, resising, drawing, opening, editing and saving pictures
os.chdir("C:\\Users\\calen\\OneDrive\\Desktop\\OpenCV\\images\\collageIms")
path="C:\\Users\\calen\\OneDrive\\Desktop\\OpenCV\\images\\collageIms"

meanwidth=0
meanheight=0

#listdir is to list all the files in the folder and "." is the current folder that we are in
numberOfImages=len(os.listdir("."))

for file in os.listdir("."):
    img=Image.open(os.path.join(path,file))
    width,height=img.size
    meanwidth=meanwidth+width
    meanheight=meanheight+height

meanwidth=meanwidth//numberOfImages
meanheight=meanheight//numberOfImages

print(meanheight)
print(meanwidth)

for file in os.listdir("."):
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
        img=Image.open(os.path.join(path,file))
        width,height=img.size
        print(width,height)
        imgr=img.resize((meanwidth,meanheight))
        imgr.save(file,"JPEG",quality=95)
        print(img.filename.split('\\')[-1],"is resized")