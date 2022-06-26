N = int(input())
zlist = [1]*N
xylist = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i!=j and xylist[i][0] < xylist[j][0] and xylist[i][1] < xylist[j][1]:
            zlist[i] += 1
print(' '.join(map(str, zlist)))