guess = [1,2,3]
answer = [1,2,3]
sum=0
for i in range(len(guess)):
    if guess[i]==answer[i]:
        sum+=1
print(sum)