array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

def count_sort():
    cnt = [0 for _ in range(max(array)+1)]
    for i in array:
        cnt[i] += 1
    for i in range(len(cnt)):
        for j in range(cnt[i]):
            print(i,end=' ')

count_sort()