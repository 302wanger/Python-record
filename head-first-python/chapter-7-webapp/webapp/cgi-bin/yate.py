# -*- coding: utf-8 -*-
# 从标准库的“string”模块中导入"Template"类。它支持简单的字符串替换模版
from string import Template
# 这个函数需要一个（可选的）字符串作为参数，用它来创建一个CIG "Content-type"行，参数缺省值是“text/html”
def start_response(resp="text/html"):
    return('Content-type: ' + resp + '\n\n')

# 打开模版文件，读入文件，换入所提供的“标题”
def include_header(the_title):
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title))
# 打开模版文件，读入文件，换入"the_links"中提供的html链接字典
def include_footer(the_links):
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return(footer.substitute(links=link_string))
# 返回表单最前面的html，允许调用者指定URL(表单数据将发送到这个url)，还可以指定所要使用的方法
def start_form(the_url, form_type="POST"):
    return('<form action="' + the_url + '" method="' + form_type + '">')
# 返回表单末尾的html标记，同时还允许调用者定制表单“submit”（提交）按钮的文本
def end_form(submit_msg="Submit"):
    return('<p></p><input type=submit value="' + submit_msg + '"></form>')
# 给定一个单选按钮和值，创建一个html单选键
def radio_button(rb_name, rb_value):
    return('<input type="radio" name="' + rb_name +
                             '" value="' + rb_value + '"> ' + rb_value + '<br />')

# 给定一个项列表。这个函数会把列表转换为一个html无序列表。
# 一个简单的for循环就可以完成全部工作，每次迭代会向ul元素增加一个li元素
def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return(u_string)

# 返回并创建一个html标题标记，默认为2级标题。"header_text"参数是必要的
def header(header_text, header_level=2):
    return('<h' + str(header_level) + '>' + header_text +
           '</h' + str(header_level) + '>')

# 用html段落标记包围一个文本段（一个字符串）
def para(para_text):
    return('<p>' + para_text + '</p>')
