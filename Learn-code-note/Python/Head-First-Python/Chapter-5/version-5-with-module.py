# 将with操作进行方法定义
# 这样会简单许多

# 以后只要有重复的操作，都可以进行方法的定义来进行简化代码



#  转换文档内容格式的方法
def sanitize(time_string):
    if '-' in time_string:     # 使用in检查字符串是否包含一个短横线或冒号
        spliter = '-'
    elif ':' in time_string:
        spliter = ':'
    else:
        return(time_string)     # 如果字符串不需要清理，就什么也不做
    (mins, secs) = time_string.split(spliter)  # 分解字符串，抽出分钟和秒部分
    return(mins + '.' + secs)

# 删除重复项的方法
def unique_item(all_item):
    unique_jam = []
    for each_item in all_item:
        if each_item not in unique_jam:
            unique_jam.append(each_item)
    return(unique_jam)

# 打开文档的方法函数
def get_coach_data(filename):            #  接受一个文件名作为唯一的参数
    try:
        with open(filename) as f:        # 打开文件，读取数据
            data = f.readline()
        return(data.strip().split(','))  # 将数据返回前先进行去除空白符/分解处理
    except IOError as ioerr:
        print('File error' + str(ioerr))      # 如果有错误，通知用户
        return(None)                          # 同时返回"None"来指示失败


path = [
'/Users/wangyuan/Desktop/Learn-code-note/Python/Head-First-Python/Chapter-5/james.txt',
'/Users/wangyuan/Desktop/Learn-code-note/Python/Head-First-Python/Chapter-5/julie.txt',
'/Users/wangyuan/Desktop/Learn-code-note/Python/Head-First-Python/Chapter-5/mikey.txt',
'/Users/wangyuan/Desktop/Learn-code-note/Python/Head-First-Python/Chapter-5/sarah.txt'
]

james = get_coach_data(path[0])
julie = get_coach_data(path[1])
mikey = get_coach_data(path[2])
sarah = get_coach_data(path[3])




# 通过列表推导方法将代码简化
clean_james = [sanitize(each_item) for each_item in james]
clean_julie = [sanitize(each_item) for each_item in julie]
clean_mikey = [sanitize(each_item) for each_item in mikey]
clean_sarah = [sanitize(each_item) for each_item in sarah]


#

unique_james = unique_item(clean_james)
unique_julie = unique_item(clean_julie)
unique_mikey = unique_item(clean_mikey)
unique_sarah = unique_item(clean_sarah)

print(sorted(unique_james)[0:3])
print(sorted(unique_julie)[0:3])
print(sorted(unique_mikey)[0:3])
print(sorted(unique_sarah)[0:3])
