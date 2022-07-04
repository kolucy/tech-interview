from itertools import permutations
N = int(input())
N_list = [i for i in range(1, N+1)]
for i in list(permutations(N_list)):
    for j in i:
        print(j, end=' ')
    print()

# 풀이2
# n = int(input())
# temp = []

# def dfs():
#     if len(temp) == n:
#         print(*temp)
#         return
#     for i in range(1, n + 1):
#         if i not in temp:
#             temp.append(i)
#             dfs()
#             temp.pop()

# dfs()