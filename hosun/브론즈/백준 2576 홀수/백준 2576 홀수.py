import sys
sys.stdin = open('input.txt')

score = 0
mm = 100
for i in range(7):
    n = int(input())
    if n % 2 != 0:
        score += n
        if n < mm:
            mm = n
if score == 0:
    print(-1)
else:
    print(score)
if score != 0:
    print(mm)
