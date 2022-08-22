n = int(input())
cnt = 0

#00시~23시
for i in range(n + 1):
    ##00분~59분
    for j in range(60):
        #00초~59초
        for k in range(60):
            #ex)05시 40분 13초 -> '054013'안에 '3'있는지 확인
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

print(cnt)
