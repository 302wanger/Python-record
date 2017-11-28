# -*- coding: utf-8 -*-
# 这个版本要解决最后一个数据是列表而不是元素的bug 
# 通过二层嵌套达到了显示每一个元素的目的

movies = [
	"The Holy Grail",1975,
	"The Life of Brain",1976,
	["Michal Palin","John Cleese",1789]
	]

# 使用内建函数isinstance()来判断
# names = ["hello", "world"]
# isinstance(names, list)   判断names列表是否是列表
# True                      是的话就进行一些运算


# 代码如下
for each_item in movies:
	if isinstance(each_item, list):
		for nested_item in each_item:
			print(nested_item)
	else:
		print(each_item)


