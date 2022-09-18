import sys
sys.stdin = open('input.txt')

N, M, B = map(int, input().split())
ground = []
for i in range(N):
    lst = list(map(int, input().split()))
    ground += lst
time = 99999999
height = 0
for i in range(257):
    block = B
    i_time = 0
    for j in ground:
        if j > i:
            block += (j - i)
            i_time += (j - i) * 2
        elif j < i:
            block -= (i - j)
            i_time += (i - j)
    if block >= 0 and time >= i_time:
        time = i_time
        height = i
print(time, height)
