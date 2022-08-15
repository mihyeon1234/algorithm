import copy
import sys
sys.stdin = open('input.txt')

n = int(input())
s_lst = list(map(int, input().split()))
p = int(input())
for i in range(p) :
    A, B = map(int, input().split())
    if A == 1 :
        for j in range(1, n + 1) :
            if j % B == 0 :
                if s_lst[j-1] == 0 :
                    s_lst[j-1] = 1
                else : 
                    s_lst[j-1] = 0 
                   # [0, 0, 1, 0, 0, 1, 0, 1]
    else : 
        sw_lst = copy.deepcopy(s_lst)
        for k in range(1, n + 1) :
            if (B - 1) - k >= 0 and (B - 1) + k <= n :
                if sw_lst[(B - 1) - k] == sw_lst[(B - 1) + k] :
                    if sw_lst[(B - 1) - k] == 0 :
                        sw_lst[(B - 1) - k] = 1 
                        sw_lst[(B - 1) + k] = 1 
                    else :
                        sw_lst[(B - 1) - k] = 0 
                        sw_lst[(B - 1) + k] = 0 
                else :
                    break
            else :
                break

        if s_lst != sw_lst :
            if sw_lst[B - 1] == 0 :
                sw_lst[B - 1] = 1
            else :
                sw_lst[B - 1] = 0
        s_lst = sw_lst

print(s_lst)
