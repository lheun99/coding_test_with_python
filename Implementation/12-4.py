#시계 방향 90도 회전 함수
def rotate_a_matrix_by_90_degree(a):
    n = len(a)  #행
    m = len(a[0])  #열

    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]

    return result


#자물쇠의 중간 부분이 모두 1인지 확인 : 열쇠로 자물쇠를 열 수 있는 상태
def check(new_lock):
    lock_length = len(new_lock) // 3

    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


#최종 코드
def solution(key, lock):
    n = len(lock)
    m = len(key)

    #자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    #새로운 자물쇠(3배 자물쇠)의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    #각 4가지 방향에서 한 칸씩 이동해보며 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)  #열쇠 회전

        #!헷갈리는 부분 + 1부터 시작해도 되는 것 아닌가 궁금하다
        for x in range(n * 2):
            for y in range(n * 2):
                #자물쇠 + 열쇠
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                #자물쇠 + 열쇠의 결과가 모두 1인지 확인
                if check(new_lock) == True:
                    return True

                #아니라면, 자물쇠 + 열쇠 값에서 열쇠 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False


print(
    solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
             [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
