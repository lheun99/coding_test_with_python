n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)

num_one = data[0]
num_two = data[1]

result = 0

while True:
    for _ in range(k):
        if m == 0:
            break
        result += num_one
        m -= 1

    if m == 0:
        break
    result += num_two
    m -= 1

print(result)
