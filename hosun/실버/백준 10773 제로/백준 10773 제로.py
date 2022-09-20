import sys
sys.stdin = open('input.txt')

K = int(input())
stk = []
for i in range(K):
    N = int(input())
    if N != 0:
        stk.append(N)
    else:
        stk.pop()
print(sum(stk))