# s = "K1:L2"
s = "A1:F1"
res = []
s = s.split(':')
# print(s)
m,n= s[0][0],s[1][0]
while m<=n:
    a,b= int(s[0][1]),int(s[1][1])
    while a<=b:
        res.append(m+str(a))
        a+=1
    m= chr(ord(m)+1)
print(res)
# return res
