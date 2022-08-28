import sys
sys.stdin = open('input.txt')

N = int(input())
num = list(map(int, input().split()))
ans_M = 0
ans_m = 0
M = 0
M_cnt = 0
m = max(num)
m_cnt = 0
for i in num:
    if i >= M:
        M = i
        M_cnt += 1
        if i == num[-1]:
            if ans_M < M_cnt:
                ans_M = M_cnt
    else:
        M = i
        if ans_M < M_cnt:
            ans_M = M_cnt
        M_cnt = 1
for j in num:
    if j <= m:
        m = j
        m_cnt += 1
        if j == num[-1]:
            if ans_m < m_cnt:
                ans_m = m_cnt
    else:
        m = j
        if ans_m < m_cnt:
            ans_m = m_cnt
        m_cnt = 1
print(max(ans_M, ans_m))