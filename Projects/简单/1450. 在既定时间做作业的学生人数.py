#枚举法
startTime = [9,8,7,6,5,4,3,2,1]
endTime = [10,10,10,10,10,10,10,10,10]
queryTime = 5
sum_out = 0
for i in range(len(startTime)):
    if startTime[i]<=queryTime<=endTime[i]:
        sum_out+=1
# return sum_out
print(sum_out)