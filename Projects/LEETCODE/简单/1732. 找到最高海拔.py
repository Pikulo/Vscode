# 有一个自行车手打算进行一场公路骑行，这条路线总共由 n + 1 个不同海拔的点组成。自行车手从海拔为 0 的点 0 开始骑行。
# 给你一个长度为 n 的整数数组 gain ，其中 gain[i] 是点 i 和点 i + 1 的 净海拔高度差（0 <= i < n）。请你返回 最高点的海拔 。

# 1. We first initialize an array of size n+1 with all zeros.
# 2. We then iterate through the gain array and calculate the cumulative sum.
# 3. We then iterate through the cumulative sum array and find the maximum sum.
gain = [-5,1,5,0,-7]
# gain = [-4,-3,-2,-1,4,3,2]
hight = [0]*(len(gain)+1)
# Time Complexity: O(n)
for i in range(len(gain)):
    if i+1 <= len(gain):
        hight[i+1]=gain[i]+hight[i]
print(max(hight))
# return max(hight)