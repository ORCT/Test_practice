n = int(input())
list = [input().split() for _ in range(n)]
list = sorted(list, key=lambda x:int(x[1]))
for i in range(n):
    print(list[i][0], end = ' ')