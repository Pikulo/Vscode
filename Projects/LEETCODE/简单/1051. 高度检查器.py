# heights = [1,1,4,2,1,3]
# heights = [5,1,2,3,4]
heights = [1,2,3,4,5]
expected = sorted(heights)
print(expected)
sum_out = 0
for i in range(len(heights)):
    if heights[i]!=expected[i]:
        sum_out+=1
# return sum_out
print(sum_out)