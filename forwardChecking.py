from domains import getDomain

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
    return
     

def setDomains(board):
    # sets values  
    for i in range(len(board)):
        for j in range(len(board[0])):
            if "." in board[i][j]:
                board[i][j] = getDomain(board,(i,j))
    # print("hello")
    