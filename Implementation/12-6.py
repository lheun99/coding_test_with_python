#구조물을 설치 혹은 삭제했을 때, 조건에 부합하는지를 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        #기둥 설치 시에
        if stuff == 0:
            #정상 설치 경우
            # 1) 바닥 설치 |
            # 2) 보 오른쪽 설치 _|
            # 3) 보 왼쪽 설치 |_
            # 4) 다른 기둥 위에 설치 :
            if y == 0 or ([x - 1, y, 1] in answer) or ([
                    x, y, 1
            ] in answer) or ([x, y - 1, 0] in answer):
                continue
            #위에 해당되지 않는 비정상 설치 경우
            return False

        #보 설치 경우
        elif stuff == 1:
            #정상 설치 경우
            # 1) 보의 왼쪽에 기둥 존재 |-
            # 2) 보의 오른쪽에 기둥 존재 -|
            # 3) 양쪽에 보가 존재 - - -
            if ([x, y - 1, 0] in answer) or ([x + 1, y - 1, 0] in answer) or (
                ([x - 1, y, 1] in answer) and ([x + 1, y, 1] in answer)):
                continue
            #위에 해당되지 않는 비정상 설치 경우
            return False

    #다 통과했다면 가능한 경우이다
    return True


def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, stuff, operate = frame

        #구조물을 삭제하는 경우
        if operate == 0:
            #삭제를 먼저 진행하고
            answer.remove([x, y, stuff])
            #삭제를 진행한 최종 구조물이 조건에 부합하는지 확인한다
            if not possible(answer):
                #부합하지 않는 경우 삭제한 구조물을 다시 설치한다
                answer.append([x, y, stuff])

        #구조물을 설치하는 경우
        if operate == 1:
            #설치를 먼저 진행하고
            answer.append([x, y, stuff])
            #설치를 진행한 최종 구조물이 조건에 부합하는지 확인한다
            if not possible(answer):
                #부합하지 않는 경우 설치한 구조물을 다시 삭제한다
                answer.remove([x, y, stuff])

    #최종 구조물 리스트를 정렬하여 출력한다
    return sorted(answer)


print(
    solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1],
                 [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))

print(
    solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1],
                 [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0],
                 [1, 1, 1, 0], [2, 2, 0, 1]]))
