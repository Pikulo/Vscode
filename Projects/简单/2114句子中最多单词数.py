from itertools import count


sentences = ["please wait", "continue to fight", "continue to win"]
sum=[]
for i in sentences:
    sum.append(i.count(' ')+1)
print(sum)
print(max(sum))
print(sentences[0].split())