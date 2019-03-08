#encoding=utf-8
from win32com import client as wc
import os
import docx

def TestDoc(filename):
    print(filename)
    dfile = os.path.splitext(filename)
    w = wc.Dispatch('Word.Application')
    newfile = "".join((dfile[0], ".docx"))
    print(111111111111111111111111)
    doc = w.Documents.Open(filename)
    print(22222222222222222222222)
    doc.SaveAs(newfile)
    print(33333333333333333333333)
    print(newfile)

if __name__ == '__main__':
    filename = "E:\\SVN\\2019\\20190110\\特色业务平台\\fbap.20190110r.t10\\XQ-2018-820\\TS_76562_20190110_回退手册.doc"
    TestDoc(filename)