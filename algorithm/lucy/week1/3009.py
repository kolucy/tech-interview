a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
g = h = 0
listx = [a, c, e]
listy = [b, d, f]
for i in listx:
    if listx.count(i) == 1:
        g = i
for j in listy:
    if listy.count(j) == 1:
        h = j
print(g, h)

# 풀이2
# listx = []
# listy = []
# for _ in range(3):
#     x, y = map(int, input().split())
#     listx.append(x)
#     listy.append(y)
# for i in range(3):
#     if listx.count(listx[i]) == 1:
#         x = listx[i]
#     if listy.count(listy[i]) == 1:
#         y = listy[i]
# print(x, y)