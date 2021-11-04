
# 1|2|3
# 4|5|6
# 7|8|9
# find out boundaries of the triplet
def getBoundary(num):
    a=num//3
    return (a*3,(a+1)*3)

def notInSquare(board,cs,string_i):
    ans = []
    xb = getBoundary(cs[0])
    yb = getBoundary(cs[1])
    for i in range(xb[0],xb[1]):
        for j in range(yb[0],yb[1]):
            if board[i][j]==string_i:
                return False
    return True
def notInCol(board,cs,string_i):
    return string_i not in [x[cs[1]] for x in board]

def notInRow(board,cs,string_i):
    return string_i not in board[cs[0]]


def getDomain(board,cs):
    ans = []
    # checking if numbers from 1 ... 9
    for i in range(1,10):
        string_i = str(i)
        # if i is not in row/column/3x3 matrix
        if notInRow(board,cs,string_i) and notInCol(board,cs,string_i) and  notInSquare(board,cs,string_i):
            ans.append(string_i)
    return ans