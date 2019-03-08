#encoding=utf-8
import pytesseract
from PIL import Image
import os

def printWords(dirs, im):
    print(dirs)
    print(im)
    os.chdir(dirs)
    img = Image.open(im)
    return pytesseract.image_to_string(img, lang='chi_sim')
    # return pytesseract.image_to_string(img, 'chi_sim')

if __name__ == '__main__':
    dirs = 'F:\黄小宝的宝\测试目录\新建文件夹'
    im = '20180204163301747.png'
    # im = '123.pdf'
    t = printWords(dirs, im)
    print(t)
    for s in t.split('\n'):
        print('---------------------->>', s)
    print(type(t))