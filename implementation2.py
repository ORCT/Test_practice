#1000000
n = int(input())
cnt = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            t = str(i)+str(j)+str(k)
            if t.count('3') != 0:
                cnt += 1
print(cnt)