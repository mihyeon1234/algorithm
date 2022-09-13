import sys
sys.stdin = open('input.txt')

T = int(input())

lst = list(map(int, input().split()))
lst_2 = [0] * T
lst_2[0] += lst[0]
for i in range(1, T):
    if lst[i] == 1:
        if lst[i - 1] == 1:
            lst_2[i] += (lst_2[i - 1] + 1)
        else:
            lst_2[i] += 1
print(sum(lst_2))

