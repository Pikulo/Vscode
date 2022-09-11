moves = "UD"
moves = "LL"
moves = "LDRRLRUULR"
res1 = 0
res2 = 0
for i in moves:
    if i == 'U':
        res1+=1
    if i == 'D':
        res1-=1
    if i == 'L':
        res2+=1
    if i == 'R':
        res2-=1
if res1 == 0 and res2==0:
    print(True)
    # return True
else:
    print(False)
    # return False