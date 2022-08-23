# s = "RLRRLLRLRL"
s = "RLLLLRRRLR"
a=0
b=0
res = 0
for i in s:
    if i =='L':
        a+=1
    else:
        b+=1
    if a==b:
        res+=1
        a=b=0
print(res)
# return res
