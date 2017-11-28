#coding:utf-8
import jieba
import os
from collections import Counter

"""
# file_object = open('caipintext.txt','r')
caipin_dictory = []
f = open('caipintext.txt',mode='r',encoding='utf-8')
for line in f.readlines():
    try:
        caipin_dictory.append(line.replace("\n",""))         #line带"\n"
    except Exception as e:
        print(e)
        pass
f.close()
"""


# open the txt and print it in one by one
f = open("caipintext.txt",'r',encoding='utf-8').readlines()

# delete the \n
b = [i.replace("\n","") for i in f]

# jieba b
jieba_b =[]
for i in range(0,len(b)):
    seg_list = jieba.cut(b[i], cut_all=False)
    jieba_b.append("/".join(seg_list))


"""
# print word_before and word_after
for i in range(0,len(b)):
    before_a = b[i]
    after_a = "/".join(jieba.cut(before_a, cut_all=False))
    print("Before:\t\t %s  \n\n After:\t\t %s \n\n" % (before_a,after_a))

# print word_before and word_after

for i in range(0,len(b)):
    print(b[i] +"\n" + jieba_b[i] + "\n")

"""
# for count the number
all_a = []

for i in b:
    k = []
    g = jieba.cut(i,cut_all=False)                                              # use jieba to handle the every line and return a generator
    for x in g:
        k.append(x)
    all_a.append(k)

all_in_one =[]
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            all_in_one.append(each_item)
print_lol(all_a)


# delete the jiebe one word
# all_in_one_two= []
while i < len(all_in_one):
    if len(all_in_one[i])==1:
        all_in_one.remove(all_in_one[i])
    else:
        pass

# use Counter to get the number of each elements
word_counts = Counter(all_in_one)
# Top 50 words
top_fifty = word_counts.most_common()


#----------------------------------------------------------------------------------


# use jieba
# first jieba result
all_a = []
all_b= []
for i in b:
    k = []
    g = jieba.cut(i,cut_all=False)                                              # use jieba to handle the every line and return a generator
    for x in g:
        k.append(x)
    p=[k,i]
    all_a.append(p)
    all_b.append(k)

# let two level list into one level
all_in_one = []
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            all_in_one.append(each_item)
# get the one level list all_in_one
print_lol(all_a)

# use Counter to get the number of each elements
word_counts = Counter(all_in_one)
# Top 50 words
top_fifty = word_counts.most_common(50)


f2 = open('capin_end.txt','w',encoding='utf-8')
f2.write(str(top_fifty))
f2.close()
