N, M = map(int, input().split())
board = list()
for _ in range(N):
    board.append(input())
chess = list()
for i in range(N-7):
    for j in range(M-7):
        idx1 = 0
        idx2 = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2 == 0:
                    if board[k][l] != 'W':
                        idx1 = idx1+1
                    if board[k][l] != 'B':
                        idx2 = idx2+1
                else:
                    if board[k][l] != 'B':
                        idx1 = idx1+1
                    if board[k][l] != 'W':
                        idx2 = idx2+1
        chess.append(min(idx1, idx2))
print(min(chess))