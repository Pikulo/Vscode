operations = ["++X","++X","X++"]
sum=0
for i in operations:
    if i=='--X' or i=='X--':
        sum-=1
    else:
        sum+=1
print(sum)

