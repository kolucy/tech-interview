import itertools

N, M = map(int, input().split())
sum_list = []
nlist = list(map(int, input().split()))
case = list(itertools.combinations(nlist, 3))
for s in range(len(case)):
    sum = 0
    for i in case[s]:
        sum += i
    if sum <= M :
        sum_list.append(sum)
print(max(sum_list))