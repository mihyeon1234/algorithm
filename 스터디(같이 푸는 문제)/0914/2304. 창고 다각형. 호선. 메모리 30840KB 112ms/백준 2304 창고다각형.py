import sys
sys.stdin = open('input.txt')

N = int(input())
lst = []
for i in range(N):
    rc = list(map(int, input().split()))
    lst.append(rc)
lst.sort()
stk = 0
area = 0
while len(lst) > 1:
    if lst[0][1] < lst[-1][1]:
        if lst[0][1] <= stk:
            del lst[0]
        else:
            area += ((lst[0][1] - stk) * (lst[-1][0] - lst[0][0] + 1))
            stk = lst[0][1]
            del lst[0]
    else:
        if lst[-1][1] <= stk:
            del lst[-1]
        else:
            area += ((lst[-1][1] - stk) * (lst[-1][0] - lst[0][0] + 1))
            stk = lst[-1][1]
            del lst[-1]
print(area + lst[0][1] - stk)