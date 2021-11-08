from forwardChecking import forwardCheck,setDomains
from domains import getDomain
from chooseEmpty import getEmptyCell
         



def solveSudoku( board,x) -> None:
    setDomains(board)
    recursiveSudoku(board,x)
    for r in board: print(r,"\n")
    print("Overall steps", x[0],"\n\n\n")
        

def recursiveSudoku(board,x) -> None:
    x[0]+=1
    # get empty cell
    verbose = False
    if x[0]<6: verbose = True
    currentCell,degree = getEmptyCell(board,verbose)

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
            print("Step\t\t",x[0],"\nVariable\t",currentCell,"\nDomain size\t",len(queue),"\nDegree\t\t",degree,"\nValue\t\t", val)
            # print(x[0],currentCell, val)
            # for r in board: print(r,"\n")            
            print("=================================")
            print("=================================")

        # returns board when the assignments are complete
        if recursiveSudoku(board,x): return board
        # print("backtracking", currentCell)
        # removing assignment and reversing forwardchecking
        board[currentCell[0]][currentCell[1]] = tmpVal
        forwardCheck(board,currentCell)

    return False

if __name__ == "__main__":
    board1 = [
    [".",".","1",".",".","2",".",".","."],
    [".",".","5",".",".","6",".","3","."],
    ["4","6",".",".",".","5",".",".","."],
    [".",".",".","1",".","4",".",".","."],
    ["6",".",".","8",".",".","1","4","3"],
    [".",".",".",".","9",".","5",".","8"],
    ["8",".",".",".","4","9",".","5","."],
    ["1",".",".","3","2",".",".",".","."],
    [".",".","9",".",".",".","3",".","."]
    ]
    board2 = [
    [".",".","5",".","1",".",".",".","."],
    [".",".","2",".",".","4",".","3","."],
    ["1",".","9",".",".",".","2",".","6"],
    ["2",".",".",".","3",".",".",".","."],
    [".","4",".",".",".",".","7",".","."],
    ["5",".",".",".",".","7",".",".","1"],
    [".",".",".","6",".","3",".",".","."],
    [".","6",".","1",".",".",".",".","."],
    [".",".",".",".","7",".",".","5","."]
    ]
    board3 = [
    ["6","7",".",".",".",".",".",".","."],
    [".","2","5",".",".",".",".",".","."],
    [".","9",".","5","6",".","2",".","."],
    ["3",".",".",".","8",".","9",".","."],
    [".",".",".",".",".",".","8",".","1"],
    [".",".",".","4","7",".",".",".","."],
    [".",".","8","6",".",".",".","9","."],
    [".",".",".",".",".",".",".","1","."],
    ["1",".","6",".","5",".",".","7","."]
    ]
    x=[0]
    # solveSudoku(board1,x) 
    x=[0]
    solveSudoku(board2,x)
    x=[0]
    # solveSudoku(board3,x)
    
    
    
