import sys
from collections import deque
ssr = sys.stdin.readline

n,m = map(int, ssr().split())
board = [list(map(int, ssr().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def sol(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if board[nx][ny] == 0:
                continue
            if board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx,ny))
    return board[n-1][m-1]

print(sol(0,0))