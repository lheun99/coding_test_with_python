n = int(input())  #보드의 크기
k = int(input())  #사과의 개수
data = [[0] * (n + 1) for _ in range(n + 1)]  #맵 리스트 (1,1 부터 시작하므로 n+1로)
info = []  #방향 회전 정보 저장 리스트

#맵 리스트에 사과가 있는 좌표 = 1로 표시해준다
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

#방향 회전 정보 리스트에 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

#방향 정보 저장_동쪽을 보고 시작하므로 시계 방향으로 동->남->서->북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


#L_왼쪽, D_오른쪽 90도 회전
#L(왼쪽 회전) : 0->3, 1->0, 2->1, 3->2
#D(오른쪽 회전) : 0->1, 1->2, 2->3, 4->0
def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

    return direction


#시뮬레이션 시작
def simulate():
    x, y = 1, 1  #시작 위치 (뱀의 머리)
    data[x][y] = 2  #뱀이 존재하는 위치는 2로 표시
    direction = 0  #처음에는 동쪽을 보고 시작한다 [0, 1]
    time = 0  #시간 (result)
    index = 0  #회전 수
    q = [(x, y)]  #뱀 정보 (꼬리가 앞쪽_queue처럼)

    while True:
        #뱀(의 머리가) 이동할 좌표
        nx = x + dx[direction]
        ny = y + dy[direction]
        #(이동한) 뱀이 맵 안에 위치하고, 몸통과 만나지 않는다면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            #사과가 없는 경우 -> 아동하고 꼬리는 없앤다
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                #이동한 좌표 = 뱀의 머리
                q.append((nx, ny))
                #뱀의 꼬리 (q의 맨 앞) 제거
                #머리 밖에 없는 경우에도 머리의 이동으로 pop이 필요함
                px, py = q.pop(0)
                #뱀의 꼬리를 없애줬으니 해당 좌표의 값을 2 -> 0으로 바꿔준다
                data[px][py] = 0

            #사과가 있는 경우 -> 이동하고 꼬리 제거하지 않는다
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                #이동한 좌표 = 뱀의 머리
                q.append((nx, ny))

        #(이동한) 뱀이 벽이나 몸통과 만난다면
        else:
            time += 1
            #끝난다
            break

        #이동 관련 작업 후
        #다음 위치로 머리를 이동시킨다
        x, y = nx, ny
        time += 1
        #회전할 시간인 경우 회전을 해준다
        #회전 수가 채워지지 않았고 and 현재 시간이 회전 리스트에 적혀있는 시간이라면
        if index < l and time == info[index][0]:
            #새로운 방향은 = turn(현재 방향, L또는D_회전할 방향)
            direction = turn(direction, info[index][1])
            #총 회전수 + 1
            index += 1

    #break을 통해 나온 최종 시간
    return time


print(simulate())
