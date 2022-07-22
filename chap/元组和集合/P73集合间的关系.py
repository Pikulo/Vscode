# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/1/25  12:13
s1={10,20,30,40}
s2={20,10,40,30}
print(s1==s2)#True
'''一个集合是否为另一个集合的子集issubset()'''

s5={90,50}
s6={100,99}
print(s4.issubset(s3))
print(s5.issubset(s3))
'''一个集合是否为另一个集合的超集issuperset()'''
print(s3.issuperset(s4))
print(s3.issuperset(s5))
'''判断是否有交集isdisjoint()'''
print(s5.isdisjoint(s3))#False表示没有交集不成立，即有交集
print(s6.isdisjoint(s3))#True表示没有交集成立







