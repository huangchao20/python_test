import os
import re


def listFiles(dirPath):
    fileList = []

    for root, dirs, files in os.walk(dirPath):
        for fileObj in files:
            fileList.append(os.path.join(root, fileObj))

    return fileList


def main():
    fileDir = "C:\\Users\\zoujiaqing\\Desktop\\Classes"

    fileList = listFiles(fileDir)

    for fileObj in fileList:
        if not re.match(r'.+\.h', fileObj, re.M | re.I):
            continue

        replace_str = fileObj.replace(fileDir + '\\', "");
        print
        '#include "' + replace_str + '"';

        for replaceFile in fileList:
            if not re.match(r'.+(\.h|\.c|\.cpp|\.hpp)', replaceFile, re.M | re.I):
                continue

            f = open(replaceFile, 'r')
            file_content = f.read()
            f.close()

            find_str = re.sub(r'.+\\(\w+\.h)', r'\1', replace_str);
            file_content = file_content.replace('"' + find_str + '"', '"' + replace_str.replace('\\', '/') + '"');

            f = open(replaceFile, 'w')
            f.write(file_content)
            f.close()


if __name__ == '__main__':
    main()