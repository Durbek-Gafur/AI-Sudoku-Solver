from domains import getDomain,getBoundary

# updates  domains of unassigned cells (row,col,triplet) after a new value has been assigned to current cell
def forwardCheck(board,cs):
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
    # updating domain of triplet 
    xb = getBoundary(cs[0])
    yb = getBoundary(cs[1])
    for i in range(xb[0],xb[1]):
        if i == cs[0]: continue
        for j in range(yb[0],yb[1]):
            if j == cs[1]: continue
            if isinstance(board[i][j],list):
                board[i][j] = getDomain(board,(i,j))  
    return
     
# analyzes row/col/triplet and adds possible values to the domain of every unassigned cell.
def setDomains(board):
    # sets values  
    for i in range(len(board)):
        for j in range(len(board[0])):
            if "." in board[i][j]:
                board[i][j] = getDomain(board,(i,j))
    