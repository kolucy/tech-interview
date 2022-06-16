import sys
N = int(sys.stdin.readline())
listn = [0] * 10001
for _ in range(N):
    listn[int(sys.stdin.readline())] += 1
for i in range(10001):
    if listn[i] != 0:
        for j in range(listn[i]):
            print(i)