# -*- coding: utf-8 -*-
# 这个是第一章的列表的知识
# 向列表中添加新的元素

# 这是老的列表
movies = ["The Holy Grail","The Life of Brain","The Meaning of Life"]

print(movies)
#  方法1
# 添加新元素
movies.insert(1,1975)  # 将1975添加到第2个位置
movies.insert(3,1976)  # 将1976添加到第4个位置
movies.insert(5,1983)  # 将1983添加到第6个位置

print(movies)

# 方法2
# 直接在列表中进行更新
movies = [
	"The Holy Grail",1975,
	"The Life of Brain",1976,
	"The Meaning of Life",1983
]

print(movies)

# 方法1和方法2在元素不多的情况下都可以使用。

# 迭代的学习
fav_movies = ["The Holy Grail", "The Life of Brain"]
print(fav_movies[0]) # 在屏幕上显示各项列表的值
print(fav_movies[1])

# 该迭代列表中的数据了
# 使用for循环进行列表的迭代，适用于任意大小的列表
for each_filck in fav_movies:
	print(each_filck)

# 同时可以用while循环进行同样的迭代
count = 0
while count < len(movies):
	print(movies[count])
	count = count + 1



# 在列表中存储列表
movies = [
	"The Holy Grail",1975,
	"The Life of Brain",1976,
	["Michal Palin","John Cleese",1789]
	]
print(movies[4][1]) # 嵌套在某个列表中的列表，而该列表本身又嵌套在另一个列表中。

# 通过for循环来迭代新的movies列表
for each_item in movies:
	print(each_item)
# 迭代结果显示最后一行没有迭代元素，而是迭代出了一个列表，这是不对的。











