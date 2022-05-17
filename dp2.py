'''n = int(input())
m = n+1
cnt = 0
while n != 1:
    a,b,c,d = m,m,m,m
    if n%5==0:
        a = n//5
    if n%3==0:
        b = n//3
    if n%2==0:
        c = n//2
    if not n%5==0 and n%3==0 and n%2==0:
        d = n-1
    n = min(a,b,c,d)
    cnt += 1
print(cnt)'''
#이렇게 풀면 어째서 값이 내가 원하는대로 나오지 않을까?
#합리적인 판단없이 그냥 조건에 만족하면 계산을 해버리기 때문
#사실 여기서 크게 안바꾸고 구현하는 방법은 모든 경우를 비교한다음 가능한 경우에서 나온 가장 작은 수를 쓰면 됨
#두 번 이상을 진행한 다음에 회귀하는 시스템이 없으면 해결 안됨
#드래그 한다음에 어퍼스트로피 치면 드래그 한 부분 전부다 문자열로 해줌
n = int(input())

table = [0 for _ in range(30001)]

for i in range(2,n+1):
    table[i] = table[i-1]+1
    if i%2 == 0:
        table[i] = min(table[i], table[i//2]+1)
    if i%3 == 0:
        table[i] = min(table[i], table[i//3]+1)
    if i%5 == 0:
        table[i] = min(table[i], table[i//5]+1)

print(table[n])