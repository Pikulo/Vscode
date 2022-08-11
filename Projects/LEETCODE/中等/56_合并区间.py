# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
# 请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
# intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,3]]
# intervals = [[1,4],[4,5]]
# intervals = [[2,6],[1,3],[8,10],[15,18]]
# intervals = [[1,4],[0,2],[3,5]] # 未考虑到的情况——两两合并后还能再合并。
intervals = [[2, 3], [4, 5], [6, 7], [8, 9],
             [1, 10]]  # 我使用的是两两匹配机制，导致奇数项最后一项无数可匹配。

# 考虑递归,结束递归的条件是？？——没有可合并对象。——通过判断list_out是否减少来决定递归条件。
# 两两比较不行

res = []
sorted_interval = sorted(intervals, key=lambda x: x[0])
print(sorted_interval)
n = len(sorted_interval)
for i in range(n):
    if i == 0:
        res.append(sorted_interval[0])
    else:
        interval = sorted_interval[i]
        print(res[-1][1], interval[0])
        if res[-1][1] >= interval[0]:
            res[-1][1] = res[-1][1] if res[-1][1] >= interval[1] else interval[1]
        else:
            res.append(interval)
print(res)


'''New ideea:fail'''
# def convert(intervals):
#     list_out  = []
#     i = 0
#     while i < len(intervals):
#         if i+1 < len(intervals):
#             k = i+1
#             while k < len(intervals):
#                 if set(range(intervals[i][0],intervals[i][1]+1)) & set(range(intervals[k][0],intervals[k][1]+1)): # 别进行两两比较
#                     list_out.append([min(intervals[i][0],intervals[k][0]),max(intervals[i][1],intervals[k][1])])
#                     del intervals[i]
#                     del intervals[k]

#                 else:

#         else:
#             pass


# def convert(intervals):
#     list_out  = []
#     i = 0
#     while i < len(intervals):
#         if i+1 < len(intervals):
#             k = i+1
#             while k < len(intervals):
#                 if set(range(intervals[i][0],intervals[i][1]+1)) & set(range(intervals[k][0],intervals[k][1]+1)): # 别进行两两比较
#                     list_out.append([min(intervals[i][0],intervals[k][0]),max(intervals[i][1],intervals[k][1])])

#                 else:
#                     k+=1

#         else:
#             list_out.append(intervals[i])
#             break
#     return list_out
# index = convert(intervals)
# while True:
#     if len(convert(index)) < len(index):
#         index = convert(index)
#     else:
#         print(convert(index))
#         break


# return  list_out
# &用于集合求交集。
# print(set(range(1,4))&set(range(2,7)))
