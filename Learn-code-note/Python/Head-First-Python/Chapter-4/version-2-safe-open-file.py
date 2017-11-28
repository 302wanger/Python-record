# 第二个版本
# 增加了打开目标文件的try/except循环
# 保证将处理出来的数据存储到目标文件

man = []
other = []
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
				other.append(line_spoken)
		except ValueError:
			pass
	data.close()
except IOError:
	print('The datafiel is missing!')

try:
    # 打开这两个文件
    man_file = open('/Users/wangyuan/Desktop/Learn-code-note/Python/Head-First-Python/Chapter-4/man_data.txt', 'w')
    other_file = open('/Users/wangyuan/Desktop/Learn-code-note/Python/Head-First-Python/Chapter-4/the_other.txt', 'w')
    # 使用print()将指定的列表保存到列表指定的磁盘文件
    print(man, file=man_file)
    print(other, file=other_file)

    # 关闭文件
    man_file.close()
    other_file.close()
except IOError:
    print('File error')