# seats = [2,2,6,6]
# students = [1,3,2,6]
seats = [4,1,5,9]
students = [1,3,2,6]
seats=sorted(seats)
students=sorted(students)
sum_data=0
for i in range(len(students)):
    sum_data+=abs(students[i]-seats[i])
print(sum_data)

#leetcode解法
print(sum(abs(students[i]-seats[i]) for i in range(len(students))))