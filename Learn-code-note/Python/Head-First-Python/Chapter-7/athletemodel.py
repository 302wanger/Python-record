#!/usr/bin/python
# -*- coding: utf-8 -*-
import pickle
from athletelist import AthleteList

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return(AthleteList(templ.pop(0), templ.pop(0), templ))
    # class AthleteList 已经写好，并放在同一文件夹内
    except IOError as ioerr:
        print('File error (get_coach_data): ' + str(ioerr))
        return(None)

def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath  # 建立一个字典all_athletes，键是ath.name（即实例的属性），值是实例本身，这样就可以通过名字找到实例了

    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
        # 存储这个字典到pickle中
    except IOError as ioerr:
        print('File error (put_and_store): ' + str(ioerr))
    return(all_athletes)  # 返回这个字典

def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)  # 只需将整个 pickle读入字典
    except IOError as ioerr:
        print('File error (get_from_store): ' + str(ioerr))
    return(all_athletes)   #  返回字典

# 以下为测试

the_files = ['james.txt', 'julie.txt', 'mikey.txt', 'sarah.txt']
data = put_to_store(the_files)
print(data)

print('-----------------')
for each in data:
    print(data[each].name + ' ' + data[each].dob)
print('-----------------')
for each in data:
    print(each)
print('-----------------')
for each in data:
    print(data[each])




