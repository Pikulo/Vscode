# nums = [12,345,2,6,7896]
nums = [555,901,482,1771]
sum_out=0
for i in nums:
    if len(str(i))%2==0:
        sum_out+=1
# return sum_out
print(sum_out)