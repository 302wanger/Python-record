# -*- coding: utf-8 -*-
#-----------------------------------------------------
#   功能：将txt文本进行分词处理
#   作者：chenbjin
#   日期：2014-07-14
#   语言：Python 3.0
#
#   使用：python fenci.py file.txt
#-----------------------------------------------------
import jieba
import sys
import importlib


def fenci(argv) :
    filename = argv[1]
    f = open(filename,'r',encoding='utf-8')
    file_list = f.read()
    f.close()

    seg_list = jieba.cut(file_list,cut_all=False)

    tf={}
    for seg in seg_list :
        #print seg
        seg = ''.join(seg.split())
        if (seg != '' and seg != "\n" and seg != "\n\n") :
            if seg in tf :
                tf[seg] += 1
            else :
                tf[seg] = 1

    f = open("result.txt","w+",encoding='utf-8')
    for item in tf:
        #print item
        f.write(item+"  "+str(tf[item])+"\n")    # return the word and the word's number
        #f.write(item + "\n")  # just return the word
    f.close()

if __name__ == '__main__' : fenci(sys.argv)
