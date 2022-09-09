from itertools import permutations as pm


def solution(n, weak, dist):
    length = len(weak)
    #원형의 길이를 2배로 늘려서 원형을 일자 형태로 만든다
    #ex) 1 3 4 9 10 -> 1 3 4 9 10 13 15 16 21 22
    for i in range(length):
        weak.append(weak[i] + n)

    #투입할 친구의 최소값을 구하기 때문에 최대 임시값은 최대 친구 수 + 1로 해준다
    answer = len(dist) + 1

    #원형에서 기존의 숫자들을 시작점으로 정할 수 있다
    #weak 리스트에서 idx가 0부터 len-1
    #1 3 4 9 10 13 15 16 21 22 -> 1 3 4 9 10
    for start in range(length):
        #친구들을 모두 나열하는 경우들에 대해 각가 확인
        for friends in list(pm(dist, len(dist))):
            #투입할 친구의 수
            cnt = 1

            #해당 친구가 점검할 수 있는 범위
            #시작할 취약점 + 친구가 점검할 수 있는 거리
            position = weak[start] + friends[cnt - 1]

            #시작하는 취약점부터 모든 취약 지점을 확인
            #ex) start = 4 -> 4 9 10 13 15
            for index in range(start, start + length):
                #해당 친구가 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    #새로운 친구를 투입한다
                    cnt += 1
                    #더 이상 투입이 불가능 하다면
                    #(=투입하는 친구의 수가 친구의 수를 넘어버리면)종료한다
                    if cnt > len(dist):
                        break

                    #투입이 가능한 경우
                    #새로 투입된 친구가 점검할 수 있는 거리로 업데이트
                    position = weak[index] + friends[cnt - 1]

            #최소값을 구한다
            answer = min(answer, cnt)

    #모든 친구로도 불가능 경우 -1을 출력한다
    if answer > len(dist):
        return -1

    return answer


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
