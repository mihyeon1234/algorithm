import sys
sys.stdin = open('inin.txt')


N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()
for i in lst:
    print(i[0], i[1])