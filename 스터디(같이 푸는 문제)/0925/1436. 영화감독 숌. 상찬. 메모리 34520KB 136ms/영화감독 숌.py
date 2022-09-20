import sys
from collections import deque

n = int(sys.stdin.readline())
a = '666'                                           # 666을 넣어준 변수
li = [str(i) for i in range(10)]                    # 각 자리수에 들어갈 0 ~ 9까지의 숫자
result = deque()                                    # dq를 통한 시간 절약
def perm(n, m):                                     # 순열 진행
    if n == m:
        result.append(int(''.join(chosen)))         # chosen 내부 원소가 모두 선택되면 result에 추가
        return
    else:
        flag = True                                 # a가 있는지 없는지 신호하는 변수
        for j in range(len(li)):                    # 0 ~ 9까지 넣을 예정
            if chosen[n] == a:                      # 만약 넣을 곳에 a가 있으면 flag에 신호주고 break
                flag = False
                break
            else:
                chosen[n] = li[j]                   # a가 없으면 10자리 아무거나 뽑기 진행
            perm(n + 1, m)
        if not flag:                                # a가 있을 경우에는 다음 자리로 넘어가 뽑기 진행
            perm(n + 1, m)

for k in range(5):                                  # 뽑아줄 총 자리수
    chosen = [-1] * 5
    chosen[k] = a
    perm(0, 5)

print(sorted(set(result))[n - 1])


