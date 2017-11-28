# 打开读取四个文件中的数据，然后进行打印


#  转换文档内容格式的方法
def sanitize(time_string):
    if '-' in time_string:     # 使用in检查字符串是否包含一个短横线或冒号
        spliter = '-'
    elif ':' in time_string:
        spliter = ':'
    else:
        return(time_string)     # 如果字符串不需要清理，就什么也不做
    (mins, secs) = time_string.split(spliter)  # 以splitter为基准，分解字符串，抽出分钟和秒部分
    return(mins + '.' + secs)

with open('/Users/wangyuan/Desktop/Head-First-Python/Chapter-5/james.txt') as jam:
    data = jam.readline()                                                           # 读取数据
james = data.strip().split(',')                                                     # 去空白，转换为一个列表
with open('/Users/wangyuan/Desktop/Head-First-Python/Chapter-5/julie.txt') as jul:
    data = jul.readline()
julie = data.strip().split(',')
with open('/Users/wangyuan/Desktop/Head-First-Python/Chapter-5/mikey.txt') as mik:
    data = mik.readline()
mikey = data.strip().split(',')
with open('/Users/wangyuan/Desktop/Head-First-Python/Chapter-5/sarah.txt') as sar:
    data = sar.readline()
sarah = data.strip().split(',')

# 对文件内容格式进行统一转化，以方便比较
clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

for each_item in james:
    clean_james.append(sanitize(each_item))
for each_item in julie:
    clean_julie.append(sanitize(each_item))
for each_item in mikey:
    clean_mikey.append(sanitize(each_item))
for each_item in sarah:
    clean_sarah.append(sanitize(each_item))

#
print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))
