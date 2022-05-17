def solution(dist):
    answer = [[]]
    #dist[i][j] = distance
    for i in range(len(dist)):
        tmp = [dist[i][0]]
        for j in range(1,len(dist)):
            if dist[i][j] >= dist[i][j-1]:
                tmp.append(j)
            else:
                end = tmp.pop()
                tmp.append(j)
                tmp.append(end)
        answer.append(tmp)
            #가까운 쪽에다 붙이기
        
    return answer[1:]

dist = [[0,5,2,4,1],[5,0,3,9,6],[2,3,0,6,3],[4,9,6,0,3],[1,6,3,3,0]]
print(solution(dist))

#브루트포스
#놓는 순서만 신경쓰면 됨
#그래프?
#이분탐색?
#정렬?
#1. 일단 기준점을 하나 잡자
#2. i,j 끼리의 값을 비교해서 작은 쪽을 가까이에 집어넣는 방식
#3. 재귀로 해서 완성이 안되면 None을 리턴하고 완성이 된 경우만 추리기 그냥 반복으로 해도 될듯
#4. index를 번호로 해서 길이로 번호를 정렬 데이터는 10000개 크기 범위는 1억
#