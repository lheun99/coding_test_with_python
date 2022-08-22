n = int(input())
plans = input().split()
x, y = 1, 1

#U, D, L, R (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
direction = ['U', 'D', 'L', 'R']

for plan in plans:
    for i in range(len(direction)):
        if plan == direction[i]:
            move_x = x + dx[i]
            move_y = y + dy[i]
    if move_x < 1 or move_y < 1 or move_x > n or move_y > n:
        #정해진 공간을 벗어나므로 위치를 업데이트 해주지 않아도 된다
        continue

    x, y = move_x, move_y

print(x, y)
