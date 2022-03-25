import sys
ssr = sys.stdin.readline

n,k = map(int,ssr().split())
cnt1=0
cnt2=0
while n>1:
    if n%k==0:
        n//=k
        cnt2+=1
    else:
        n-=1
        cnt1+=1
print(cnt1+cnt2)