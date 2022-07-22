#平面上有 n 个点，点的位置用整数坐标表示 points[i] = [xi, yi] 。
# 请你计算访问所有这些点需要的 最小时间（以秒为单位）。
# 你需要按照下面的规则在平面上移动：
#     每一秒内，你可以：
#         沿水平方向移动一个单位长度，或者
#         沿竖直方向移动一个单位长度，或者
#         跨过对角线移动 sqrt(2) 个单位长度（可以看作在一秒内向水平和竖直方向各移动一个单位长度）。
#     必须按照数组中出现的顺序来访问这些点。
#     在访问某个点时，可以经过该点后面出现的点，但经过的那些点不算作有效访问。

#思路：计算插差值
points = [[559,511],[932,618],[-623,-443]]
i=0
sum=0
while(i<len(points)):
    if i+1<len(points):
        list1=points[i]
        list2=points[i+1]
        print(list1,list2)
        a=min(abs(list1[0]-list2[0]),abs(list1[1]-list2[1]))
        #注意b这儿是绝对值差的绝对值
        b=abs(abs(list1[0]-list2[0])-abs(list1[1]-list2[1]))
        print(a,b)
        sum+=a
        sum+=b
    i+=1
# return sum
print(sum)

    

