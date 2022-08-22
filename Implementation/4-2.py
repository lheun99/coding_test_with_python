data = input()
row = int(data[1])
column = ord(data[0]) - ord('a') + 1

#가능한 방향 정리 (8가지)
moves = [(-2, -1), (2, -1), (-2, 1), (2, 1), (-1, -2), (1, -2), (-1, 2),
         (1, 2)]
cnt = 0

for move in moves:
    move_row = row + move[0]
    move_column = column + move[1]

    #이동한 위치가 왕실 정원 안에 있는 경우 = 이동할 수 있는 경우
    if move_row >= 1 and move_row <= 8 and move_column >= 1 and move_column <= 8:
        cnt += 1

print(cnt)
