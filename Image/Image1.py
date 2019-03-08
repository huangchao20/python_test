import pytesseract
from PIL import Image
import os

def printWords(dirs, im):
    print(dirs)
    print(im)
    os.chdir(dirs)
    return pytesseract.image_to_string(Image.open(im))

if __name__ == '__main__':
    dirs = 'F:\\image'
    im = 'timg6.jpg'
    t = printWords(dirs, im)
    print(t)