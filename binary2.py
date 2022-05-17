def bin(array,start, end, target):
    while start<=end:
        mid = (start + end)//2
        if array[mid] == target:
            return mid
        elif array[mid]>target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
array = list(map(int, input().split()))
m = int(input())
want = list(map(int, input().split()))

array.sort()
for i in want:
    if bin(array,0,n,i) != None:
        print('yes')
    else:
        print('no')