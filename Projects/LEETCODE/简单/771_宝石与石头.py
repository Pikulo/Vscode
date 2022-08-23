jewels = "aA"
stones = "aAAbbbb"
res = 0
for i in stones:
    if i in jewels:
        res+=1
print(res)
