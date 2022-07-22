# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/1/25  12:30
# '''交集'''
# s1={10,20,30,40,50,60}
# s2={20,30,99}
# print(s1.intersection(s2))
# print(s1 & s2)       # &与intersection等价，都是求交集
# '''并集'''
# print(s1.union(s2))
# print(s1 | s2)      # |和union等价，求并集
# # & |操作后的原集合不变化
# '''差集'''
# print(s1.difference(s2))  # 从s1中去掉s1&s2的部分
# print(s1-s2)
# print(s2.difference(s1))  # 从s2中去掉s1&s2的部分
# print(s2-s1)
'''对称差集'''
s1={10,20,30,40,50,60}
s2={20,30,99}
print(s1.symmetric_difference(s2))  #s1&s2之外的元素的并集
print(s1 ^ s2)








