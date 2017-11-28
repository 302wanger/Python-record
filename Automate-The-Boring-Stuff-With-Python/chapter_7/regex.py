# -*- coding: utf-8 -*-

# 正则表达式使用步骤
# 1.用import re 导入正则表达式模块
# 2.用re.compile()函数创建一个Regex对象（记得使用原始字符串）
# 3.向Regex对象的search()方法传入想查找的字符串。它返回一个Match对象。
# 4.调用Match对象的group()方法，返回实际匹配文本的字符串




import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('my number is 415-555-4242.')
print('phone number found: '+ mo.group())

# 结果应该为：
# phone number found: 415-555-4242
