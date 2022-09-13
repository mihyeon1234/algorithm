import sys
sys.stdin = open('input.txt')


M = 0
cnt = 0
for T in range(10):
    outt, inn = map(int, input().split())
    cnt -= outt
    cnt += inn
    if cnt > M:
        M = cnt
print(M)