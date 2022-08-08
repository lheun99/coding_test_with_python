n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    print("t >>", target)
    result += (n - target)
    print("r >>", result)
    n = target
    print("n >>", n)

    if n < k:
        break
    result += 1
    print("r2 >>", result)
    n //= k
    print("n2 >>", n)
    print()
result += (n - 1)
print("result >>", result)
