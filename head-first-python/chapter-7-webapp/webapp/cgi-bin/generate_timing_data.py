#! /usr/local/bin/python3
# -*- coding: utf-8 -*-
# 只有基于 unix的系统才需要第一行代码

import cgi
import athletemodel
import yate
#  启用python的cgi跟踪技术
import cgitb
cgitb.enable()

# 从模型得到数据
athletes = athletemodel.get_from_store()

# 确定处理的是哪个选手的数据
form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))
# 获取选手的名字和出生日期
print(yate.header("Athlete: "+athlete_name+",DOB:"+athletes[athlete_name].dob +"."))
print(yate.para("The top times for this athlete are:"))
# 将前3个时间转换为一个无序的html列表
# 由于top3这个方法生命线为“@property”，在这种情况下不需要括号
print(yate.u_list(athletes[athlete_name].top3))
# 这个web页面的最下面有两个链接，最后一个链接返回前一个cgi脚本
print(yate.include_footer({"Home":"/index.html","Select another athlete":"generate_list.py"}))
