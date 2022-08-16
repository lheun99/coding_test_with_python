#https://school.programmers.co.kr/learn/courses/30/lessons/42891?language=python3

import heapq


def solution(food_times, k):
    if sum(food_times) < k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, food_times[i], i + 1)  #[음식 시간, 음식 번호]

    ate_times = 0  #음식 먹은 시간 합
    pre_times = 0  #직전에 다 먹은 음식 시간
    length = len(food_times)  #남은 음식의 개수

    while ate_times + ((q[0][0] - pre_times) * length) <= k:
        #ate_times + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수
        now = heapq.heappop(q)[0]
        ate_times += (now - pre_times) * length
        length -= 1
        pre_times = now

    result = sorted(q, key=lambda x: x[1])
    return result[(k - ate_times) % length][1]
