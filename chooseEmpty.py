from collections import defaultdict
from domains import getDomain,getBoundary

def MRV(board):
    minLen = 100
    ans = defaultdict(list)
    ans[100].append((-1,-1))
    for i in range(len(board)):
        for j in range(len(board[0])):
            if isinstance(board[i][j],list) or "."==board[i][j]: #remove .
                clen = len(board[i][j])
                if clen <= minLen:
                    ans[clen].append((i,j))
                    minLen = clen
                    minim = (i,j)
    # print("minLen ",minLen)
    return ans[minLen]


def countUnassigned(board,cs):
    counter = 0
    i=cs[0]
    # unassigneds in a row
    for j in range(len(board[i])): 
        if isinstance(board[i][j],list) : counter+=1 #or "."==board[i][j]
    j = cs[1]
    # unassigneds in a col
    for i in range(len(board)): 
        if isinstance(board[i][j],list) or "."==board[i][j]:  counter+=1   

    # updating domain of triplet 
    xb = getBoundary(cs[0])
    yb = getBoundary(cs[1])
    for i in range(xb[0],xb[1]):
        if i == cs[0]: continue
        for j in range(yb[0],yb[1]):
            if j == cs[1]: continue
            if isinstance(board[i][j],list) : counter+=1 #or "."==board[i][j]   
    return counter-2
    # get the number of unassigned values for each mrv
def degreeHeuristic(board, mrv):
    ans = defaultdict(list)
    mx = -float("inf")
    # mn = float("inf")
    for cell in mrv:
        count = countUnassigned(board,cell)
        ans[count].append(cell)
        mx = max(mx,count)
        # mn = min(mn,count)
        # break
    # print("max constraints ", mx,ans)
    return ans[mx]

def getEmptyCell(board):
    mrv = MRV(board)
    if mrv[0][0]==-1:
        return mrv[0]
    degreeHeuristicVal = degreeHeuristic(board,mrv)
    # print("mrv->",mrv,"dh->",degreeHeuristicVal)
    # for key in tmp: print(key, tmp[key])
    return degreeHeuristicVal[0]

# bboard=[["5","3",".",".","7",".",".",".","."],
#         ["6",".",".","1","9","5",".",".","."],
#         [".","9","8",".",".",".",".","6","."],
#         ["8",".",".",".","6",".",".",".","3"],
#         ["4",".",".","8",".","3",".",".","1"],
#         ["7",".",".",".","2",".",".",".","6"],
#         [".","6",".",".",".",".","2","8","."],
#         [".",".",".","4","1","9",".",".","5"],
#         [".",".",".",".","8",".",".","7","9"]]
# print(getEmptyCell(bboard))