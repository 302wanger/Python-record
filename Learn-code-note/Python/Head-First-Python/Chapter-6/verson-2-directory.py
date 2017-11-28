# 用字典来实现新数据的更方便导入

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

def get_caoch_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return(data.strip().split(','))
    except IOError as ioerror:
        print('File error: '+ str(ioerror))
        return(None)

sarah = get_caoch_data('sarah2.txt')

# 创建一个字典
sarah_data ={}
sarah_data['Name'] = sarah.pop(0)   # pop()方法为抽出第一个元素，然后哈希给一个元素
sarah_data['DOB'] = sarah.pop(0)    # 继续抽取第一个元素
sarah_data['Times'] = sarah         # 剩下的就是
print(sarah_data['Name'] + "'s fastest times are: " + str(sorted(set(sanitize(t) for t in sarah_data['Times']))[0:3]))