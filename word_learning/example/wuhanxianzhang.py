#coding= utf-8
import jieba
import jieba.posseg as pseg


# open the file
# and print every line
string = open('ten_line.txt', 'r', encoding='utf-8').readlines()

# fenci
words = pseg.cut(string)

# save the result
result = ""
for w in words:
    result += str(w.word) + "/" + str(w.flag)

f=open('result_ten.txt','w')
f.write(result)
f.close()
