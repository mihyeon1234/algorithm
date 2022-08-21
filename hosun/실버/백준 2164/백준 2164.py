import sys
sys.stdin = open('백준 2164.txt')
from collections import deque

N = int(input())
lst = deque()
for i in range(N, 0, -1):
    lst.append(i)
while len(lst) > 1:
    lst.pop()
    lst.insert(0, lst[-1])
    lst.pop()
print(lst[0])