# 这是第三个版本，
# 为了防治在关闭文件前发生错误，使用finally来进行处理
# 即无论是否发生错误，都将进行关闭文件操作


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
    man_file = open('/Users/wangyuan/Desktop/Head-First-Python/Chapter-4/man_data.txt', 'w')
    other_file = open('/Users/wangyuan/Desktop/Head-First-Python/Chapter-4/the_other.txt', 'w')
    # 使用print()将指定的列表保存到列表指定的磁盘文件
    print(man, file=man_file)
    print(other, file=other_file)  # 如果这个地方发生问题，就尴尬了，所以要引入finally方法

except IOError:
    print('File error')
# 关闭文件的操作被放在了finally逻辑中
# 这样无论发生何种错误，都回执行close操作
finally:
	if 'man_file' in locals():
		man_file.close()
	if 'other_file' in locals():
		other_file.close()



