def solution(s):
    answer = len(s)
    
    #step -> 자르는 단위 
    for step in range(1, len(s)//2+1):
        #압축된 문장
        compressed = ""
        prev = s[0:step] #단위만큼 잘린 첫번째 문자열
        cnt = 1
        
        #단위만큼 잘라가면서 동일한 문자열이 나오는지 확인
        for j in range(step, len(s), step): #step ~ len(s)까지 step만큼 증가하면서
            #이전 문자열과 동일하다면 cnt 증가
            if prev == s[j:j+step]:
                cnt += 1
            #동일하지 않다 -> 압축 불가 
            else:
                #최종 압축본에 해당 문자열 추가
                compressed += str(cnt) + prev if cnt >= 2 else prev
                #상태 초기화:
                #이전까지 동일했던 prev를 더 이상 사용하지 않고, 
                #새로운 prev로 바꿔준다
                prev = s[j:j+step]
                cnt = 1    
        #남아있는 문자열 처리
        compressed += str(cnt) + prev if cnt >= 2 else prev
        #최종적으로 압축된 문자열이 가장 짧은 것이 answer
        answer = min(answer, len(compressed))
        
    return answer

print(solution("aabbcccc"))