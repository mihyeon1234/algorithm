import sys

w, h = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

x = p + t                   # x만큼 간 길이
y = q + t                   # y만큼 간 길이

x1 = x // w                 # 가로길이로 간 만큼의 거리를 나눈 몫이 가로의 출발선을 결정
y1 = y // h                 # 세로길이로 간 만큼의 거리를 나눈 몫이 세로의 출발선을 결정

if x1 % 2:                  # 홀수는 오른쪽에서 출발
    ans_x = w - (x % w )
else:                       # 짝수는 왼쪽에서 출발
    ans_x = x % w

if y1 % 2:                  # 홀수는 위쪽에서 출발
    ans_y = h - (y % h)
else:
    ans_y = y % h           # 짝수는 아래쪽에서 출발

print(ans_x, ans_y)         # 최종 좌표값 출력