import sys
ssr = sys.stdin.readline

n,m = map(int, ssr().split())
result = []
for i in range(n):
    result.append(min(list(map(int, ssr().split()))))
print(max(result))