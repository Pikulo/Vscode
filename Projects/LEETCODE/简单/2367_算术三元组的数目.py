from codecs import namereplace_errors
from typing import Counter


nums = [0,1,4,6,7,10]
diff = 3
nums = [4,5,6,7,8,9]
diff = 2
res = 0
for i in nums:
    if i-diff in nums and i+diff in nums:
        res+=1
        s.append(i)
print(res)
# return res