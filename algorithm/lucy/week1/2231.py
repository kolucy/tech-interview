N = int(input())
Mlist = []
for M in range(N) :
    m = str(M)
    sum = M
    for s in m:
        sum += int(s)
    if sum == N:
        Mlist.append(M)
if len(Mlist) == 0:
    print(0)
else:
    print(min(Mlist))