import sys
sys.stdin = open('백준 1244.txt')

N = int(input())
sw_lst = list(map(int, input().split()))
p = int(input())
for i in range(p):
    A, B = map(int, input().split())
    if A == 1:
        for j in range(1, N + 1):
            if j % B == 0:
                if sw_lst[j - 1] == 0:
                    sw_lst[j - 1] = 1
                else:
                    sw_lst[j - 1] = 0
                    # [0, 0, 1, 0, 0, 1, 0, 1]
    else:
        for k in range(1, (N-1) // 2):
            if (B - 1) - k >= 0 and (B - 1) + k <= N - 1:
                if sw_lst[(B - 1) - k] == sw_lst[(B - 1) + k]:
                    if sw_lst[(B - 1) - k] == 0:
                        sw_lst[(B - 1) - k] = 1
                        sw_lst[(B - 1) + k] = 1
                    else:
                        sw_lst[(B - 1) - k] = 0
                        sw_lst[(B - 1) + k] = 0
                else:
                    break
        if sw_lst[B - 1] == 0:
            sw_lst[B - 1] = 1
        else:
            sw_lst[B - 1] = 0

for i in range(len(sw_lst)):
    if i % 10 == 9:
        print(sw_lst[i], end='\n')
    else:
        print(sw_lst[i], end=' ')