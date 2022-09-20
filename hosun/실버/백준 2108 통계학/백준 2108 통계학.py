import sys

N = int(sys.stdin.readline())
lst = list(int(sys.stdin.readline()) for _ in range(N))
lst.sort()

print(round(sum(lst) / N))
print(lst[N // 2])

cnt = [0] * 8001
zero = 4000
for i in range(N):
    cnt[lst[i] + zero] += 1
cnt_max = max(cnt)
if cnt.count(cnt_max) == 1:
    print(cnt.index(cnt_max) - zero)
else:
    cnt.remove(cnt_max)
    print(cnt.index(cnt_max) + 1 - zero)

print(lst[-1] - lst[0])