words = ["pay","attention","practice","attend"]
pref = "at"
# words = ["leetcode","win","loops","success"]
# pref = "code"
sum_out = 0
for i in words:
    print(i[:len(pref)])
    if i[:len(pref)]==pref:
        sum_out+=1
print(sum_out)
# return sum_out
#法2startwith()
for i in words:
    print(i.startswith(pref))