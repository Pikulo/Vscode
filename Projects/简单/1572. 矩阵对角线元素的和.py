# mat = [[1,2,3],
#        [4,5,6],
#        [7,8,9]]
# mat = [[5]]
mat = [ [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]]
if len(mat)==1:
    # returm mat[0][0]
    print(mat[0][0])
else:
    sum_out=0
    i=0
    j=len(mat)-1
    while(i<len(mat)):
        sum_out+=mat[i][i]+mat[i][j]
        i+=1
        j-=1
    if len(mat)%2!=0:
        sum_out-=mat[len(mat)//2][len(mat)//2]
    # return sum_out
    print(sum_out)
print(1&1)