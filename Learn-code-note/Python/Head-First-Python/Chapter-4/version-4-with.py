# 使用with来替代finally的功能
# with会减少代码量
# with妥善关闭一个可能打开的数据文件

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


# 使用with替换 finally逻辑
# 不用操心文件close的问题
try:
    with open('/Users/wangyuan/Desktop/Head-First-Python/Chapter-4/man_data.txt', 'w') as man_file:
        print(man, file=man_file)
    with open('/Users/wangyuan/Desktop/Head-First-Python/Chapter-4/the_other.txt', 'w') as other_file:
        print(other, file=other_file)
except IOError as err:
    print('File error:' + str(err))


