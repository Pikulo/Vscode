from re import A


print(2^0)
encoded = [6,2,7,3]
first = 4
ans=[]
ans.append(first)
for i in encoded:
    a=i^first
    first=a
    ans.append(a)
print(ans)
    
