words = ["abc","car","ada","racecar","cool"]
for i in words:
    print(i,i[::-1])
    if i==i[::-1]:
        print(i)
        # return i
        break
# return ''