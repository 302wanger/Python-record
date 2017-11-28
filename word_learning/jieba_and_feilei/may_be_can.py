'''
get from
http://blog.csdn.net/eastmount/article/details/50256163
'''

#encoding=utf-8
import jieba
import jieba.posseg as pseg
import jieba.analyse
# Step 1 - get the file content

# load self-def directon
jieba.load_userdict('dict.txt')

f = open('ceshi.txt','r',encoding="utf-8")
string=f.read()
# string get the list string

# Step2 - 去除停用词，清洗数据
stop_dir = ['9','听','/','1','、','瓶']
stopwords = {}.fromkeys(stop_dir)

segs = jieba.cut(string, cut_all=False)
final = ''
for seg in segs:
    if seg not in stopwords:
        final += seg

f = open('clear_final.txt','w',encoding='utf-8')
f.write(final)
f.close()

#
f = open('clear_final.txt','r',encoding="utf-8")
content = f.read()
# Step 3-2 - 开始分词
words = pseg.cut(content)

result = ""
for w in words:
#    result += str(w.word) + " " + str(w.flag)  # add word and its flag
     result += str(w.word) + " "                 # just the word

# get the fenci result and save it in a file
f = open("result_ten.txt","w",encoding='utf-8')
f.write(result)
f.close()

# 获取关键词
# Step 3-2 - select the keyword and save it to a file
tags = jieba.analyse.extract_tags(content, topK=20)

tags_word=""

for i in tags:
    tags_word += i +'\n'

f= open('tags_word.txt','w',encoding='utf-8')
f.write(tags_word)
f.close()
