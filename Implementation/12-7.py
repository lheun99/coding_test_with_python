from itertools import combinations as cb

n, m = map(int, input().split())
#치킨집, 일반집 좌표 저장 리스트
chicken, house = [], []

for r in range(n):
    #도시 정보 한 줄 (r_행)
    data = list(map(int, input().split()))

    #도시 정보 줄 당 각 데이터 (c_열)
    for c in range(n):
        #일반 집이라면 일반 집 리스트에 좌표 추가
        if data[c] == 1:
            house.append((r, c))
        #치킨 집이라면 치킨 집 리스트에 좌표 추가
        elif data[c] == 2:
            chicken.append((r, c))

#모든 치킨 집 좌표들 중에서 m개를 뽑아 가능한 모든 조합을 구한다
candidates = list(cb(chicken, m))


#조합별 치킨 거리를 구하는 역할의 함수
def get_sum(candidate):
    #각 조합별 치킨거리
    result = 0
    #각 집에 대하여
    for hx, hy in house:
        #1e9 > 가능한 최댓값이 10억 미만이라면 무한대를 나타낸다 (최대의 임시값을 설정해준다)
        temp = 1e9

        #각 집에 대하여 가장 가까운 치킨집을 찾는다
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))

        #해당 조합에 대한 최종 도시의 치킨 거리에 해당 집에 대한 치킨 거리를 구한다
        result += temp

    return result


#각 조합별 도시의 치킨 거리의 최소값을 구한다
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)
