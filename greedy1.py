'''
import sys
ssr = sys.stdin.readline
n,m,k = map(int, ssr().split())
num = list(map(int, ssr().split()))
num.sort()
result = 0
cnt = 0
while m>0:
    if cnt < k:
        result += num[len(num)-1]
        cnt += 1
    else :
        result += num[len(num)-2]
        cnt = 0
    m -= 1
print(result)
'''

'''
#another solution
import sys
ssr = sys.stdin.readline
n,m,k = map(int, ssr().split())
num = list(map(int, ssr().split()))
num.sort()
result = 0
a = m//(k+1)
b = m%(k+1)
result = a*(num[len(num)-1]*k+num[len(num)-2]) + b*num[len(num)-1]
print(result)
'''
