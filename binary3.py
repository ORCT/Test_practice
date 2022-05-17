def bin(d,m,start,end):#값으로 해야함
    while start<=end:
        mid = (start+end)//2
        ans = 0
        for i in d:
            if i >= mid:
                ans += i-mid
        if ans == m:
            return mid
        elif ans > m:
            start = mid+1
        else:
            end = mid-1
    return None
n,m = map(int, input().split())
d = list(map(int, input().split()))
print(bin(d,m,0,max(d)))