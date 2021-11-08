from collections import defaultdict
from domains import getDomain,getBoundary

    # chooses variables(cell) with the least number of values in the domain
def MRV(board,verbose):
    minLen = 100
    ans = defaultdict(list)
    ans[100].append((-1,-1))
    for i in range(len(board)):
        for j in range(len(board[0])):
            if isinstance(board[i][j],list): 
                clen = len(board[i][j])
                if clen <= minLen:
                    ans[clen].append((i,j))
                    minLen = clen
                    minim = (i,j)
    # if verbose: print("domain-size-",minLen)
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
        if isinstance(board[i][j],list):  counter+=1   

    # updating domain of triplet 
    xb = getBoundary(cs[0])
    yb = getBoundary(cs[1])
    for i in range(xb[0],xb[1]):
        if i == cs[0]: continue
        for j in range(yb[0],yb[1]):
            if j == cs[1]: continue
            if isinstance(board[i][j],list) : counter+=1 #or "."==board[i][j]   
    return counter-2

    # get the number of unassigned values for each variable returned by mrv
def degreeHeuristic(board, mrv,verbose):
    # return mrv
    ans = defaultdict(list)
    mx = -float("inf")
    # mn = float("inf")
    for cell in mrv:
        count = countUnassigned(board,cell)
        ans[count].append(cell)
        mx = max(mx,count)
        # mn = min(mn,count)
        # break
    return (ans[mx][0],mx)

    # chooses next empty cell based on MRV and Degree Heuristic
def getEmptyCell(board,verbose):
    mrv = MRV(board,verbose)
    if mrv[0][0]==-1:
        return (mrv[0],-1)
    return degreeHeuristic(board,mrv,verbose)

