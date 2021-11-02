

def getEmptyCell(board):
    minim = (-1,-1)
    minLen = 100
    for i in range(len(board)):
        for j in range(len(board[0])):
            if isinstance(board[i][j],list):
                clen = len(board[i][j])
                if clen < minLen:
                    minLen = clen
                    minim = (i,j)
    return minim

def updateDomains(board,cs=False):
    if cs:
        i=cs[0]
        for j in range(len(board[i])):
            # if the cell is empty cell
            if isinstance(board[i][j],list):
                board[i][j] = getDomain(board,(i,j))                
        j = cs[1]
        for i in range(len(board)):
            # if the cell is empty cell
            if isinstance(board[i][j],list):
                board[i][j] = getDomain(board,(i,j))   
        return
    # sets values   
    for i in range(len(board)):
        for j in range(len(board[0])):
            if "." in board[i][j]:
                board[i][j] = getDomain(board,(i,j))
    # print("hello")
                
# ARc consistency could be imporved               
def Ac3( board):
    changed = False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if "." in board[i][j]:
                d = getDomain(board,(i,j))
                if len(d)==1:
                    board[i][j]=d[0]
                    changed=True
    return changed
                
def terminalState(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] ==".":
                return False
    return True
def getBoundary(num):
    a=num//3
    return (a*3,(a+1)*3)
def square(board,cs):
    ans = []
    xb = getBoundary(cs[0])
    yb = getBoundary(cs[1])
    for i in range(xb[0],xb[1]):
        for j in range(yb[0],yb[1]):
            if board[i][j]!=".":
                ans.append(board[i][j])
    return ans
def tryAc3(board):
    changed = True
    i=0
    while changed:
        prv=getEmptyCell(board)
        changed = Ac3(board)
        i+=1
def getDomain(board,cs):
    ans = []
    for i in range(1,10):
        si = str(i)
        if si not in board[cs[0]] and si not in [x[cs[1]] for x in board] and si not in square(board,cs):
            ans.append(si)
    return ans

def solveSudoku( board) -> None:
    updateDomains(board)
    recursiveSudoku(board)
        

def recursiveSudoku( board) -> None:
    # tryAc3(board)
    cs = getEmptyCell(board)
    if cs[0]==-1: return board
    
    queue = getDomain(board,cs)
    if len(queue)==0: return False
        
    for val in queue:
        tmpVal = board[cs[0]][cs[1]]
        board[cs[0]][cs[1]] = val
        updateDomains(board,cs)
        if recursiveSudoku(board): return board
        board[cs[0]][cs[1]] = tmpVal
        updateDomains(board,cs)
    return False

if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    updateDomains(board)
    recursiveSudoku(board)
    for r in board: print(r,"\n")
