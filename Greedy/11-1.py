n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
member = 0

for i in data:
    member += 1
    if member >= i:
        result += 1
        member = 0

print(result)
