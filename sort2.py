n = int(input())
list=[]
for _ in range(n):
    list.append(int(input()))
list.sort(key = lambda x:-x)
print(*list)