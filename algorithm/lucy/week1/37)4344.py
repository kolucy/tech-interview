C = int(input())
for i in range(C):
    S = list(map(int, input().split()))
    N = S.pop(0)
    avg = (sum(S))/N
    cnt = 0
    for s in S:
        if(s > avg):
            cnt += 1
    p = cnt/N
    print(f'{round((100*p), 3)}%')