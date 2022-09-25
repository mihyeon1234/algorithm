import sys
sys.stdin = open('input.txt')

n = int(input())
stk = []
answer = []
last = 1
nono = 0
for i in range(1, n + 1):
    num = int(input())
    while last <= num:
        stk.append(last)
        answer.append('+')
        last += 1
    if stk[-1] == num:
        stk.pop()
        answer.append('-')
    else:
        print('NO')
        break
else:
    for i in answer:
        print(i)