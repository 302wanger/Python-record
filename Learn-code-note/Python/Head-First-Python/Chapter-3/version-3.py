# -*- coding: utf-8 -*-
# 特定指定异常
# 比第二个版本多了个try/except，原因是要判断文件是否能打开
# 使用try/except可以让你关注代码真正要做的工作
# 而且可以避免向程序增加不必要的代码和逻辑。


try:
	path = '//Users/wangyuan/Desktop/Learn-code-note/Python/Head-First-Python/Chapter-3/sketch.txt'
	data = open(path, 'r')

	for each_line in data:
		try:
			(role, line_spoken) = each_line.split(':', 1)
			print(role)
			print(' said: ')
			print(line_spoken)
		except ValueError:
			pass

	data.close()
except IOError:
	print("The data file is missing!")
