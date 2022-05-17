def solution(grid):
    visited = [False]*3
    for i in range(len(grid)):
        j = grid[i].find('?')
        if j != -1:
            for k in range(3):
                if not visited[k]:
                    if k == 0: 
                        grid[i][j] = 'a'#이부분을 a도 썼다가 b도 썼다가 c도 썼다가 해야하는거
                    elif k == 1:
                        grid[i][j] = 'b'
                    else:
                        grid[i][j] = 'c'
    if check(0,0) != False:
        answer += 1
    answer = -1
    return answer

def check(r,c):
    if grid[r][c] == 'a':
        grid[r][c] = 0
        check(r-1,c)
        check(r+1,c)
        check(r,c-1)
        check(r,c+1)#더 이상 주변에 a가 없으면 재귀는 끝나고
    for i in range(len(grid)):
        if grid[i].find('a') != -1:
            return False
    if grid[r][c] == 'b':
        grid[r][c] = 0
        check(r-1,c)
        check(r+1,c)
        check(r,c-1)
        check(r,c+1)#더 이상 주변에 a가 없으면 재귀는 끝나고
    for i in range(len(grid)):
        if grid[i].find('b') != -1:
            return False
    if grid[r][c] == 'c':
        grid[r][c] = 0
        check(r-1,c)
        check(r+1,c)
        check(r,c-1)
        check(r,c+1)#더 이상 주변에 a가 없으면 재귀는 끝나고
    for i in range(len(grid)):
        if grid[i].find('c') != -1:
            return False
            
grid = ["??b", "abc", "cc?"]
print(solution(grid))
#브루트포스
#어떻게 연결됐는지를 판단할것인지
#예를 들어서 a로 판단한다고 하면
#어떻게든지 a를 하나 찾은다음에 찾고 나면
#쭉 a랑 같은지 비교를 하고 방문한 애들을 다른걸로 바꾸고
#그런다음에 전체를 대상으로 검사했을 때 a가 남아있다면 다 연결이 안된 것으로 볼 수 있다
#판단용 함수를 하나 짜고
#물음표를 무엇으로 채울것인지...
#물음표 채우기 백트래킹? 아니면 브루트 포스
