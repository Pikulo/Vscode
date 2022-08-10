# nums = [2,5,6,9,10]
# nums = [7,5,6,8,3]
# The code is to find the greatest common divisor of two numbers.
# 
# Args:
#   nums: an array of integers
#   min_nums: the minimum number of times a number can be used
#   max_nums: the maximum number in the list
# Returns:
#   The number of times the number is divisible by the other numbers in the list.

# My idea
nums = [3,3]
# Time Complexity: O(n)
nums.sort()
max_nums = nums[0]
min_nums = nums[-1]
max_out = 0
print(max_nums,min_nums)
for i in range(1,min_nums+1):
    if min_nums%i == 0 and max_nums%i == 0:
        max_out=i
print(max_out)
# return max_out

# other idea
# 辗转相除法
def gcd(x, y):      # 满足 x>=y
    if y == 0:
        return x
    return gcd(y, x%y)

mx, mn = max(nums), min(nums)
# return gcd(mx, mn)
print(gcd(mx, mn))
# 更相减损术
def gcd(x, y):
    if x == y:
        return x
    if x < y:
        return gcd(y-x, x)
    return gcd(x-y, y)
mx, mn = max(nums), min(nums)
# return gcd(mx, mn)
print(gcd(mx, mn))