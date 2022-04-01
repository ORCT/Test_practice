n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for _ in range(k):
    a[a.index(min(a))],b[b.index(max(b))] = max(b),min(a)
print(sum(a))