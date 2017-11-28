import sys
import pickle

# 导入函数失败，只能将这个方法重写了
def print_lol(the_list,level=0, fn=sys.stdout):
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

new_man =[]
try:
    with open('/Users/wangyuan/Desktop/Learn-code-note/Python/Head-First-Python/Chapter-4/man_data.txt', 'rb') as man_file:
        new_man = pickle.load(man_file)
except IOError as err:
    print('File error: ' + str(err))
except pickle.PickleError as perr:
    print('Pickling error: ' + str(perr))

print_lol(new_man)