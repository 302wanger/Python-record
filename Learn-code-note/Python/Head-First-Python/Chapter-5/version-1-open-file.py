# 打开读取四个文件中的数据，然后进行打印

with open('/Users/wangyuan/Desktop/Learn-code-note/Python/Head-First-Python/Chapter-5/james.txt') as jam:
    data = jam.readline()                                                           # 读取数据
james = data.strip().split(',')                                                     # 去空白，转换为一个列表
with open('/Users/wangyuan/Desktop/Learn-code-note/Python/Head-First-Python/Chapter-5/julie.txt') as jul:
    data = jul.readline()
julie = data.strip().split(',')
with open('/Users/wangyuan/Desktop/Learn-code-note/Python/Head-First-Python/Chapter-5/mikey.txt') as mik:
    data = mik.readline()
mikey = data.strip().split(',')
with open('/Users/wangyuan/Desktop/Learn-code-note/Python/Head-First-Python/Chapter-5/sarah.txt') as sar:
    data = sar.readline()
sarah = data.strip().split(',')


print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))

