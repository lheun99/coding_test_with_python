n, m = map(int, input().split())

result = 0

for _ in range(n):
    data = list(map(int, input().split()))
    min_num = min(data)
    result = max(result, min_num)

print(result)
