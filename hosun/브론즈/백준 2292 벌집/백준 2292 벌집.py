N = int(input())

i = 1
j = 0
cnt = 1
while N > i:
    j += 6
    i += j
    cnt += 1
print(cnt)