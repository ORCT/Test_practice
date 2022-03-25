#행이랑 열을 범위를 정해놓고 범위 밖이면 무시하고 범위 안이면 카운트
col = 'abcdefgh'
pos = input()
c,r = int(col.find(pos[0])+1),int(pos[1])
step = [[c-2,r-1],[c-1,r-2],[c-2,r+1],[c+2,r-1],[c-1,r+2],[c+1,r-2],[c+2,r+1],[c+1,r+2]]
cnt = 0
for i in step:
    if i[0]>=1 and i[0]<=8 and i[1]>=1 and i[1]<=8:
        cnt += 1
print(cnt)
# print(type(c))
# print(type(r))
# print(c)
# print(r)