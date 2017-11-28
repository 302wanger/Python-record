# -*- coding: utf-8 -*-
# 将原有数据进行处理
# 将两个人的对话分为2个文件

# 对数据进行处理

# 为man和the_other分别创建一个空列表
man = []
the_other = []
try:
	path = '/Users/wangyuan/Desktop/Learn-code-note/Python/Head-First-Python/Chapter-4/sketch-2.txt'
	data =  open(path)
	for each_line in data:
		try:
			(role, line_spoken) = each_line.split(':', 1) # 以第一个：为纬度进行切割
			line_spoken = line_spoken.strip()  # 将去除空白符后的字符串再赋回到自身
			if role == 'Man':
				man.append(line_spoken)
			elif role == 'Other Man':
				the_other.append(line_spoken)
		except ValueError:
			pass
	data.close()
except IOError:
	print('The datafiel is missing!')

# 显示处理后的数据
print(man)
print(the_other)
