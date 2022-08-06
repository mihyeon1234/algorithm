x, y, w, h = map(int, input().split())
if x <= w - x and x <= y and x <= h - y :
    print(x)
elif w - x <= x and w - x <= y and w - x <= h - y :
    print(w - x)
elif y <= x and y <= w - x and y <= h - y :
    print(y)
elif h - y <= x and h - y <= w - x and h - y <= y :
    print(h - y)