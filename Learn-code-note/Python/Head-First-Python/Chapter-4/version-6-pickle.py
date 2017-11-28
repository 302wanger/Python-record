# 导入pickle模块
import pickle

# pickle 模块
# 用dump保存
# 用load恢复
# 将数据进行二进制处理，方便调用和储存



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
    with open('/Users/wangyuan/Desktop/Learn-code-note/Python/Head-First-Python/Chapter-4/man_data.txt', 'wb') as man_file: # 将访问模式改为二进制
        pickle.dump(man, file=man_file)
    with open('/Users/wangyuan/Desktop/Learn-code-note/Python/Head-First-Python/Chapter-4/the_other.txt', 'wb') as other_file:
        pickle.dump(other, file=other_file)
except IOError as err:
    print('File error:' + str(err))
# 确保不出现异常
except pickle.PickleError as perr:
    print('PickError :' + str(perr))

