# -*- encoding=utf-8 -*-
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/7/28  9:10


# 正则表达式

import re

# 创建模式对象
# 方法1
pat = re.compile('AA')  # 此处的AA是正则表达式，用来验证其他字符串
## search字符串是被校验的内容
# m=pat.search('CBA') # NONE

# m=pat.search('ABCAA') # <re.Match object; span=(3, 5), match='AA'>

# m=pat.search('ABCAADDCCAAA') #<re.Match object; span=(3, 5), match='AA'>
'''只匹配最先找到的对象'''
#方法2
# m = re.search('asd','Aasd') # <re.Match object; span=(1, 4), match='asd'>
# '''前面字符串是规则，后面是被考察的'''
# print(m)

# print(re.findall('a','ASDaDFGAa')) # 前面字符串是规则，后面字符串是被校验
# print(re.findall('a','ASDaDFGAaa'))
#
# print(re.findall('[A-Z]','ASDaDFGAa')) # 找到大写字母
# # ['A', 'S', 'D', 'D', 'F', 'G', 'A']
# print(re.findall('[A-Z]+','ASDaDFGAa'))
# # ['ASD', 'DFGA']
# print(re.findall('[^A,D]','ASDaDFGAa'))
# # ['S', 'a', 'F', 'G', 'a']
# print(re.findall('[^A,D]+','ASDaDFGAa'))
# # ['S', 'a', 'FG', 'a']

'''sub'''

print(re.sub('a','A','abcadcasd')) # 用A替换a

# 建议在正则表达式中，被比较的字符串前面加r，不用担心转义字符的问题
a = "\aabd-\'" # 不加r
# abd-'
a = r"\aabd-\'" # 加r
# \aabd-\'
print(a)






