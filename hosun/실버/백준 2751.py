import sys
N = int(sys.stdin.readline())

lst = []
for i in range(N):
  x = int(sys.stdin.readline())
  lst.append(x)
lst.sort()
for i in lst:
    print(i)