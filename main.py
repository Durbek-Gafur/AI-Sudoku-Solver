from forwardChecking import forwardCheck,setDomains
from domains import getDomain
from chooseEmpty import getEmptyCell
         



def solveSudoku( board,x) -> None:
    setDomains(board)
    recursiveSudoku(board,x)
    for r in board: print(r,"\n")
        

def recursiveSudoku(board,x) -> None:
    x[0]+=1
    # get empty cell
    verbose = False
    if x[0]<6: verbose = True
    currentCell = getEmptyCell(board,verbose)

    # no empty cells
    if currentCell[0]==-1: return board
    
    #get all possible values for current empty cell
    queue = getDomain(board,currentCell)

    # when the domain of variable is empty , we are solving in a wrong way
    if len(queue)==0: return False
    # try every value from domain
    for val in queue:
        # assinging value and forwardchecking
        tmpVal,board[currentCell[0]][currentCell[1]] = board[currentCell[0]][currentCell[1]], val
        forwardCheck(board,currentCell)
        if x[0]<6:
            print(x[0],"variable-",currentCell,"domain_size-",len(queue),"val-", val)
            print("=================================")
            print("=================================")
            # print(x[0],currentCell, val)
        # returns board when the assignments are complete
        if recursiveSudoku(board,x): return board
        # print("backtracking", currentCell)
        # removing assignment and reversing forwardchecking
        board[currentCell[0]][currentCell[1]] = tmpVal
        forwardCheck(board,currentCell)

    return False

if __name__ == "__main__":
    board = [
    ["5","3",".",".","7",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]
    ]
    
    x=[0]
    solveSudoku(board,x)
    
    print(x[0])
    
