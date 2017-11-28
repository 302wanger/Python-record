# -*- coding: utf-8 -*-
# 进行词性的分类：类似改词属于名字、动词还是其他
import jieba
import jieba.posseg as pseg



f = open('ceshi.txt','r',encoding="utf-8")
string=f.read()

words = pseg.cut(string)
result = ""
for w in words:
    result += str(w.word) + "/" + str(w.flag)  # add word and its flag
#    result += str(w.word) + "/"                 # just the word

f = open("result_ten.txt","w",encoding='utf-8')
f.write(result)
f.close()
