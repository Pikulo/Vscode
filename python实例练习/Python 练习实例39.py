# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/21  22:06
lst=[1,3,5,6,9,11,20,23]
a=int(input('请输入数\n'))
k=0
for i in range(len(lst)):
    if i<len(lst)-1:
        if lst[i] <= a <= lst[i + 1]:
            lst.insert(i+1,a)
            k=1
            break

if k==0:
    lst.append(a)
print(lst)
'''在if __name__ == 'main': 下的代码
只有在第一种情况下（即文件作为脚本直接执行）
才会被执行，而import到其他脚本中是不会被执行的。'''