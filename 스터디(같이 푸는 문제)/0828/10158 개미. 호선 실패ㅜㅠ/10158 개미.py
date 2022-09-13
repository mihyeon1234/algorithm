import sys
sys.stdin = open('input.txt')

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
x = (p + t) % w
y = (q + t) % h
print(x, y)