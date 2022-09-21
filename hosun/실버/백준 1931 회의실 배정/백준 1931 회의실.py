import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
lst = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    lst.append([a, b])

lst.sort(key = lambda x: x[0])
lst.sort(key = lambda x: x[1])

cnt = 1
end = lst[0][1]

for i in range(1,N):
    if lst[i][0] >= end:
        cnt +=1
        end = lst[i][1]

print(cnt)