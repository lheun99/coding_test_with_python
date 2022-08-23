n, m = map(int, input().split())
#방문 확인용 맵 (0->방문x, 1->방문)
visited = [[0] * m for i in range(n)]

x, y, direction = map(int, input().split())
#출발 좌표 방문 처리
visited[x][y] = 1

map = [list(map(int, input().split())) for i in range(n)]

#북동남서(0123) 방향 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


#왼쪽으로 회전 (0<-1<-2<-3)
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


#시뮬레이션
cnt = 1
turn_time = 0  #동일 죄표 상에서 4되면 처리 필요
while True:
    #현재 방향을 기준으로 왼쪽 방향부터 갈 곳을 정한다
    turn_left()
    #왼쪽 방향에 정면에 있는 좌표 (nx, ny)
    nx = x + dx[direction]
    ny = y + dy[direction]

    #정면에 있는 좌표가 가보지 않은 곳인 경우 그 곳으로 이동한다
    if visited[nx][ny] == 0 and map[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue

    #정면에 있는 좌표가 이미 가본 곳이거나 바다인 경우
    else:
        #회전 횟수만 늘어난다
        turn_time += 1

    #동일 죄표 상에서 4방향 모두 갈 수 없는 경우
    if turn_time == 4:
        #한 칸 뒤로 이동 시 좌표 (nx, ny)
        nx = x - dx[direction]
        ny = y - dy[direction]
        #뒤로 이동 시 좌표로 갈 수 있다면 이동한다
        if map[nx][ny] == 0:
            x = nx
            y = ny
        #뒤가 바다라서 이동이 불가능하면 움직임을 멈춘다
        else:
            break

        turn_time = 0

print(cnt)
