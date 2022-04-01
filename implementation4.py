import sys
ssr = sys.stdin.readline

def m1(d):
    result = (d+3)%4
    return result

def m2(r,c,d):
    global cnt
    if board[r][c-1] == 1 and board[r-1][c] == 1 and board[r][c+1] == 1 and board[r+1][c] == 1:
        cnt += 1
        return
    if d == 0:
        if board[r][c-1] == 1: 
            d = (d+3)%4
            m2(r,c,d)
        else:
            d = (d+3)%4
            board[r][c] = 1
            c -= 1
            cnt += 1
            m2(r,c,d)
    elif d == 1:
        if board[r-1][c] == 1: 
            d = (d+3)%4
            m2(r,c,d)
        else:
            d = (d+3)%4
            board[r][c] = 1
            r -= 1
            cnt += 1
            m2(r,c,d)
    elif d == 2:
        if board[r][c+1] == 1: 
            d = (d+3)%4
            m2(r,c,d)
        else:
            d = (d+3)%4
            board[r][c] = 1
            c += 1
            cnt += 1
            m2(r,c,d)
    else:
        if board[r+1][c] == 1: 
            d = (d+3)%4
            m2(r,c,d)
        else:
            d = (d+3)%4
            board[r][c] = 1
            r += 1
            cnt += 1
            m2(r,c,d)
        

n,m = map(int, ssr().split())
r,c,d = map(int, ssr().split())
board = [list(map(int, ssr().split())) for _ in range(n)]
cnt = 0
m2(r,c,d)
print(cnt)
# visited = [[0 for _ in range(m)] for _ in range(n)]
# visited[r][c] = 1
# print(visited)
'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''