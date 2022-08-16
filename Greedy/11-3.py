data = input()

cnt_0 = 0  #1->0
cnt_1 = 0  #0->1

if data[0] == '1':
    cnt_0 += 1
else:
    cnt_1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':
            cnt_0 += 1
        else:
            cnt_1 += 1

print(min(cnt_0, cnt_1))
