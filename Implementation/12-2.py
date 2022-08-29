#isdigit or isalpha
s = input()

alphabet = []
num = 0

for i in s:
    if i.isalpha():
        alphabet += i
    else:
        num += int(i)

alphabet.sort()

if num != 0:
    alphabet += str(num)

print("".join(alphabet))