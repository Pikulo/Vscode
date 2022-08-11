board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
res=True
for i in board:
    list_number=[j for j in i if j.isdigit()]
    if len(list_number)!=len(set(list_number)):
        res=False
        break
for m in zip(*board):
    list_number=[j for j in list(m) if j.isdigit()]
    if len(list_number)!=len(set(list_number)):
        res=False
        break
m=0
n=3
while m <= 6 and res:
    k=0
    while k <= 6:
        list_merge =[]
        for i in range(k,k+3):
            list_merge+=board[i][m:n]
        list_number=[j for j in list_merge if j.isdigit()]
        print(list_number)
        if len(list_number)!=len(set(list_number)):
            res=False
            break
        k+=3
    m+=3
    n+=3
if res:
    # return True
    print(True)
else:
    # return False
    print(False)
