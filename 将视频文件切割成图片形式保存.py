from PIL import Image
import cv2

def splitFrames(videoFileName):
    cap = cv2.VideoCapture(videoFIlename)

    num = 1
    while True:
        success , data = cap.read()

        if not success:
            break

        im = Image.formarray(data)
        im.save(str(num) + ".jpg")
        num = num + 1
    cap.release()
splitFrames('__name__变量的用法.avi')
