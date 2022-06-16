t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif (r1+r2)**2 == (x2-x1)**2 + (y2-y1)**2:
        print(1)
    elif (abs(r1-r2))**2 == (x2-x1)**2 + (y2-y1)**2:
        print(1)
    elif (r1+r2)**2 < (x2-x1)**2 + (y2-y1)**2:
        print(0)
    elif (x2-x1)**2 + (y2-y1)**2 < (abs(r1-r2))**2:
        print(0)
    elif x1 == x2 and y1 == y2:
        print(0)
    else:
        # abs(r1-r2) < d < r1+r2
        print(2)

# 풀이2
# import math
# n = int(input())
# for _ in range(n):
#     x1, y1, r1, x2, y2, r2 = map(int, input().split())
#     distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)  # 두 원의 거리 (원의방정식활용)
#     if distance == 0 and r1 == r2 :  # 두 원이 동심원이고 반지름이 같을 때
#         print(-1)
#     elif abs(r1-r2) == distance or r1 + r2 == distance:  # 내접, 외접일 때
#         print(1)
#     elif abs(r1-r2) < distance < (r1+r2) :  # 두 원이 서로다른 두 점에서 만날 때
#         print(2)
#     else:
#         print(0)  # 그 외에