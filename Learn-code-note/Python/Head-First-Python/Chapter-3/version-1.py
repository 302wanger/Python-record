# -*- coding: utf-8 -*-
# 这个版本的程序只是学会
# 打开文件
# 查看文件内容
# 关闭文件


# python 打开和书写文件的方法
# 打开文件
the_file = open('sketch.txt')
# Do something with the data
# in "the_file"
the_file.close()        # 关闭文件


path = '/Users/wangyuan/Desktop/Learn-code-note/Python/Head-First-Python/Chapter-3/sketch.txt'
data = open(path,'r')
print(data.readline())  # 取一行代码做测试
print(data.readline())  # 再取一行代码做测试
print("--------------------"*3)
data.seek(0)    # 使用seek()方法返回到文件起始位置
# 开始迭代文件
for each_line in data:
	print(each_line)
# 关闭文件
data.close()


