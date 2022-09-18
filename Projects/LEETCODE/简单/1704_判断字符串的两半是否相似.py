from itertools import count


s = "book"
s = "textbook"
lis = ['a','e','i','o','u','A','E','I','O','U']
n = len(s)//2
a = s[:n]
b = s[n:]
print(a,b)
cou_a = 0
cou_b = 0
for i in a:
    if i in lis:
        cou_a+=1
for i in b:
    if i in lis:
        cou_b+=1
print(cou_a==cou_b)

# other idea
lis = ['a','e','i','o','u','A','E','I','O','U']
n = len(s)//2
a = s[:n]
b = s[n:]
print(sum(i in lis for i in a)==sum(i in lis for i in b))
# return sum(i in lis for i in a)==sum(i in lis for i in b)
