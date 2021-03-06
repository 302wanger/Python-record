# -*- coding: utf-8 -*-
import sys
"""
这是"nester.py"模块，提供了一个名为print_lol()的函数
用来打印列表，其中包含或不包含嵌套列表。
"""

# 会将每一个不同数组的元素缩进一个tab 

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

"""
names = ["Aohn", "Bob", "Cav",
			["Danny","Fuk",
				["Enin","Gink"]
			]
		]
print_lol(names)
"""
