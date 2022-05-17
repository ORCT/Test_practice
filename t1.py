def solution(id_list, report, k):
    report = set(report)
    reporter = {}
    reported = {}
    answer = [0]*len(id_list)
    for i in report:
        ter,ted = i.split()
        reporter[ter] = ted
        if ted in reported:
            reported[ted] += 1
        else:
            reported[ted] = 1
    for i in reported.keys():
        if reported[i] >= k:
            for j in reporter.keys():
                if i in reporter[j]:
                    answer[id_list.index(j)] += 1
    
    return answer

id_list = ['muzi','frodo','apeach','neo']
report = ['muzi frodo','apeach frodo','frodo neo','muzi neo','apeach muzi']
k = 2

print(solution(id_list,report,k))
