#  代码优化环节

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)



def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return(
            {'Name': templ.pop(0),
             'DOB': templ.pop(0),
             'Times': str(sorted(set([sanitize(t) for t in templ]))[0:3])})
    except IOError as ioerr:
        print('File error: '+ str(ioerr))
        return(None)

# 方法更新完毕
sarah = get_coach_data('sarah2.txt')
print(sarah['Name'] + "'s fastest times are: " + sarah['Times'])



