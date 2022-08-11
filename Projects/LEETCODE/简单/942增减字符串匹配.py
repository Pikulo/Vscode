# s = "IDID"
# s = "III"
s = "DDI"

'''新思路'''
# I对应小数，D对应大数，所以用左右指针来遍历
left = 0
right = len(s)
list_out = []
for i in s:
    if i == 'I':
        list_out.append(left)
        left+=1
    else:
        list_out.append(right)
        right-=1
print(left,right)
list_out.append(left)
print(list_out)
# return list_out



'''错误了'''
# list_out = [0]*(len(s)+1)
# num_s = [i for i in range(len(s)+1)]
# print(num_s)
# # print(len(list_out))
# index = len(s)
# for i in s[::-1]:
#     print(i)
#     if i == 'I':
#         if index==len(s):
#             list_out[index-1] = min(num_s)
#             list_out[index] = max(num_s)
#             num_s.remove(min(num_s))
#             num_s.remove(max(num_s))
#         else:
#             list_out[index-1] = max(num_s)
#             num_s.remove(max(num_s))
        
#     else:
#         if index==len(s):
#             list_out[index] = min(num_s)
#             list_out[index-1] = max(num_s)
#             num_s.remove(min(num_s))
#             num_s.remove(max(num_s))
#         else:
#             list_out[index-1] = min(num_s)
#             num_s.remove(min(num_s))
#     index-=1
# print(list_out)