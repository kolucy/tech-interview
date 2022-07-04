a = []
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i != j and j != k and k != i:
                a.append([i, j, k])
for _ in range(int(input())):
    b, c, d = map(int, input().split())
    b = [b//100, (b//10)%10, b%10]
    e = []
    for i in a:
        if int(b[0] == i[0]) + int(b[1] == i[1]) + int(b[2] == i[2]) == c and int(b[0] in i[1:]) + int(b[1] in [i[0], i[2]]) + int(b[2] in i[:2]) == d:
            e.append(i)
        a = e[:]
print(len(a))