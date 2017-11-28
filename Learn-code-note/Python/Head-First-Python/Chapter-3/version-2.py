# -*- coding: utf-8 -*-
# 这个版本通过try/except 来实现异常的处理
# 跳过异常，然后运行程序

path = '/Users/wangyuan/Desktop/Learn-code-note/Python/Head-First-Python/Chapter-3/sketch.txt'
data = open(path,'r')

# 开始迭代文件
# 文档内容格式不统一，需要进行转换
for each_line in data:
	try:
		(role, line_spoken) = each_line.split(':', 1)
		print(role)
		print(' said: ')
		print(line_spoken)
	except:
		pass


data.close()

