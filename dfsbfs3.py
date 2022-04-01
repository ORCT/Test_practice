import sys
ssr = sys.stdin.readline

def sol(r,c):
    if r <= -1 or r >= n or c <= -1 or c >= m:
        return False
    if board[r][c] == 0:
        board[r][c] = 1
        sol(r-1,c)
        sol(r+1,c)
        sol(r,c-1)
        sol(r,c+1)
        return True

n,m = map(int, ssr().split())
board = [list(map(int, ssr().split())) for _ in range(n)]
result = 0
for i in range(n):
    for j in range(m):
        if sol(i,j) == True:
            result += 1        
print(result)