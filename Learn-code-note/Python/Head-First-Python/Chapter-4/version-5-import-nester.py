# 导入模块，实现文件显示的更智能
# 模块导入方法有些奇怪
# 导入同文件夹中的nester 模块
import  sys

def print_lol(the_list,level=0, fn=sys.stdout ):
	"""
	这个函数有一个位置参数，名为"the_list",
	这可以是任何python列表(包含或不包含嵌套列表)，
	所提供列表中的各个数据会（递归地）打印到屏幕上，而且各占一行。
	第二个参数（名为"level"）用来在遇到嵌套列表时插入制表符。
	"""
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item, level+1, fn)
		else:
			for tab_stop in range(level):
				print("\t", end = '', file=fn) #尴尬的python版本问题
			print(each_item, file=fn)




# 导入nester模块后，所有的print()要变成print_lol()

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
    with open('/Users/wangyuan/Desktop/Learn-code-note/Python/Head-First-Python/Chapter-4/man_data.txt', 'w') as man_file:
        print_lol(man, fn=man_file)
    with open('/Users/wangyuan/Desktop/Learn-code-note/Python/Head-First-Python/Chapter-4/the_other.txt', 'w') as other_file:
        print_lol(other, fn=other_file)
except IOError as err:
    print('File error:' + str(err))