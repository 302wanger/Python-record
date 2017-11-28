# 继承python内置的list类，会少些很多代码
# 通过类建立在内置功能上，可以利用python的强大
# 同时提供路具体应用需求的定制解决方案

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)




class AthleteList(list):
    def __init__(self, a_name, a_dob=None,a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])

vera = AthleteList('veravi')
vera.append('1.31')
print(vera.top3())
vera.extend(['1.11', '2:22', '3-33', '4:44'])
print((vera.top3()))