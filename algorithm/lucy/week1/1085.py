x, y, w, h = map(int, input().split())
a = b = 0
if w-x > x:
    a = x
else:
    a = w-x
if h-y > y:
    b = y
else:
    b = h-y
print(min(a, b))

# 풀이2
# x, y, w, h = map(int, input().split())
# print(min(x, y, w-x, h-y))