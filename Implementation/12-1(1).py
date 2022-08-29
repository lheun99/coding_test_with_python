n = input()
half = len(n) // 2

left = n[:half]
right = n[half:]

left_sum = 0
right_sum = 0

for i in range(half):
  left_sum += int(n[i])

for i in range(half,len(n)):
  right_sum += int(n[i])

if left_sum == right_sum:
  print("LUCKY")

else:
  print("READY")