import sys
sys.setrecursionlimit(10000)


def solution(n, edges, k, a, b):
    visited[a] = 1
    if a == b:
        answer = sum(visited)-1#방문노드 갯수 - 1
        return answer
    for i in range(len(edges)):
        if visited[i] == 0 and edges[i][a]:
            solution(n,edges,k,i,b)
            
visited = [0]*16


n = 8
edges = [[0,1],[1,2],[2,3],[4,0],[5,1],[6,1],[7,2],[7,3],[4,5],[5,6],[6,7]]
k = 4
a = 0
b = 3

print(solution(n,edges,k,a,b))
#그래프
#print([[False]*9]*9)