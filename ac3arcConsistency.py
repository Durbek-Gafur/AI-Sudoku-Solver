from domains import getDomain
from chooseEmpty import getEmptyCell

def tryAc3(board):
    changed = True
    i=0
    while changed:
        prv=getEmptyCell(board)
        changed = Ac3(board)
        i+=1            
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
  