# allowed = "ab"
# words = ["ad","bd","aaab","baa","badab"]
allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
print(set(allowed))
sum=0
for i in words:
    # print(set(i))
    if set(i) <=set(allowed):#判断子集
        sum+=1
print(sum)
