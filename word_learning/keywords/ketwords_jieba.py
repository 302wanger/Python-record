# -*- coding: utf-8 -*-
#-*-encoding:utf-8-*-
# 第一行是为了进行中文注释

# 获取文件中第一个名字，然后将名词写入另一个文件
import jieba.posseg as pseg
import linecache
import jieba
import time

# 获得待处理文件的行数
f_content = open("keyword.txt",'r', encoding='utf-8')
lineNum = 0
for count, line in enumerate(f_content):
    lineNum += 1

# 读取一行，将每一行的第一个名词替换为关键词，再逐行写入另一个文件
'''读取一行，把一行里面的第一个名词替换成关键词，再逐行写入另一个文件'''
i = 1
j = 1
for j in range(lineNum+1): #循环的次数等于行数，即一行执行一次如下代码
    line_content=linecache.getline('keyword.txt', i)#获取第i行内容
    string = line_content.decode('utf-8')

    #print line_content
    words = pseg.cut(string)
    result = ''
    amount = 1 #引入amount，这样就可以仅仅替换一行中出现的第一个名词，后面的不替换
    for w in words:
        if w.flag == 'n' and amount == 1:#n 是词语的属性
            amount+=1
            w.word = 'haha' #haha为要替换的关键词
        result+=str(w.word) #这个有点妙，喜欢
    f = open('keyword_result.txt','a', encoding='utf-8')
    f.write(result)
    f.close()
    i+=1
    j+=1


    #
