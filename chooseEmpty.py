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
     