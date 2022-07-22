# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/1/25  17:17

# a='hello,python'
# s=a.upper()
# print(a,id(a))
# print(s,id(s))
# print(s.lower(),id(s.lower()))
# print(a,id(a))
s='hello,Python'
'''居中对齐'''
print(s.center(20,'#'))  # 指定宽度-字符串宽度 ####hello,Python####
print(s.center(11,'#'))  # 指定宽度《字符串宽度hello,Python
'''左对齐'''
print(s.ljust(20,'#'))
print(s.ljust(8,'#'))
'''右对齐'''
print(s.rjust(20,'#'))
print(s.rjust(8,'#'))
'''右对齐，使用0进行填充'''
print(s.zfill(20))
print(s.zfill(8))

