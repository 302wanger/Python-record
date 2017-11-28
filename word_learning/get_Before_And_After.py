import jieba

# print 10 elements of b directory
before = [b[i] for i in range(0,10)]

# get the jieba result
after = [jieba.cut(str(b[i])),cut_all=False for i in range(0,10)]

# print out jieba result

for i in range(0,10):
    before_a = b[i]
    after_a = jieba.cut(before, cut_all=False)

    print("Before:\t\t %s  \n\n After:\t\t %s \n\n" % (b[i],"/ ".join(after_a)))

#    print("/ ".join(after))




#

# open the file
with open('caipintext.txt', 'r',encoding='utf-8') as f:
    date = f.readlines()

jieba_list = jieba.cut(date,cut_all=False)

tf = {}
