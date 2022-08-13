import sys
sys.stdin = open('2751.txt')


N = int(input())
lst = []
for i in range(N):
  x, y = map(int, input().split())
  lst.append([y, x])

lst.sort()
for i in lst:
    print(i[1], i[0])


# for i in lst:
#     i[0], i[1] = i[1], i[0]
# lst.sort()
# for i in lst:
#     print(i[1], i[0])