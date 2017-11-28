# -*- coding: utf-8 -*-
# 版本2中如果有大量内嵌列表的话，代码写起来会很麻烦
# 所以使用函数的方法将代码简化下


movies = [
	"The Holy Grail",1975,
	"The Life of Brain",1976,
	["Michal Palin","John Cleese",1789,
		["Interesting",1991]
	]
]

# 定义函数

def print_lol(the_list):
	for each_item in the_list:                      # 用一个for循环处理所提供的列表
		if isinstance(each_item,list):              # 如果所处理的列表项本身是一个列表
			print_lol(each_item)                    # 则调用函数
		else:
			print(each_item)                        # 如果所处理的列表项不是一个列表，则在屏幕上显示这个列表项

# 调用函数
print_lol(movies)