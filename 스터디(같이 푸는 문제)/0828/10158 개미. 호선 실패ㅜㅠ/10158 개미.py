w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]
dr = 3
x = w
y = h
dr = 0
for i in range(t):
    if 0 <= x <= w and 0 <= y <= h:
        if y == 0 and x == 0 or y == 0 and x == w or y == h and x == 0 or  y == h and x == w:
            dr = (dr + 2) % 4
        elif y == 0 or y == h:
            dr = abs(3 - dr)
        elif x == 0 or x == w:
            if dr == 0:
                dr = 1
            elif dr == 1:
                dr = 0
            elif dr == 2:
                dr = 3
            else:
                dr = 2
        nx = x + dx[dr]
        ny = y + dy[dr]
        y, x = ny, nx
print(x, y)