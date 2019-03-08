from PIL import Image, ImageFilter

# codeLib = '''@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. '''
# 字符列表
codeLib = '''@#$%&?*aeoc=<{[(/l|!-_:;,."'^~` '''
# print(len(codeLib))
# 将彩色图片转化为黑白的
# im = Image.open('reba.jpg')
# result = im.convert("L")
# result.save("result_2.jpg","jpeg")
# 计算字符列表的长度
count = len(codeLib)


# 定义转化的函数，方便在主函数一次或多次调用
def trans_photo(image_file):
    # 将彩色图片转化为黑白的图片
    image_file = image_file.convert("L")
    codePic = ''
    # 循环图片的宽高，并得到每一像素的灰度值
    for h in range(0, image_file.size[1]):
        for w in range(0, image_file.size[0]):
            gray = image_file.getpixel((w, h))
            # 将对应的灰度值映射到字符
            codePic = codePic + codeLib[int(((count) * gray) / 256)]
        # 实现每行结尾处自动换行
        codePic = codePic + '\r\n'
    return codePic


if __name__ == "__main__":
    # 以二进制读取图片文件
    fp = open('MM.png', 'rb')
    image_file = Image.open(fp)
    # 将图片进行适当的放大或者缩小
    image_file = image_file.resize((int(image_file.size[0] / 2), int(image_file.size[1] / 4)))

    # 以写的形式打开w.txt文件
    tmp = open("w.txt", "w")
    # 将最终得到的codePic写到文件中
    tmp.write(trans_photo(image_file))
    tmp.close()
