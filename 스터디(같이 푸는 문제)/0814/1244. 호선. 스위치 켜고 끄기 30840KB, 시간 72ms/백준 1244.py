import sys
sys.stdin = open('input.txt')

N = int(input())
sw_lst = list(map(int, input().split()))
p = int(input())
for i in range(p):
    A, B = map(int, input().split())
    if A == 1:                                  # 성별이 남자일 때
        for j in range(1, N + 1):
            if j % B == 0:                      # 숫자의 배수의 값을 변경
                if sw_lst[j - 1] == 0:
                    sw_lst[j - 1] = 1
                else:
                    sw_lst[j - 1] = 0

    else:                                       # 성별이 여자일 때
        for k in range(1, (N-1) // 2):          # 주어진 숫자를 기준으로 양 옆을 조사하므로, 전체의 반만 조사!
            if (B - 1) - k >= 0 and (B - 1) + k <= N - 1:   # 인덱스 오류를 피하기 위해 범위 조절
                if sw_lst[(B - 1) - k] == sw_lst[(B - 1) + k]:    # 기준 숫자의 양 옆이 같을 때
                    if sw_lst[(B - 1) - k] == 0:                  # 양 옆의 값을 변경
                        sw_lst[(B - 1) - k] = 1
                        sw_lst[(B - 1) + k] = 1
                    else:
                        sw_lst[(B - 1) - k] = 0
                        sw_lst[(B - 1) + k] = 0
                else:
                    break
            if sw_lst[B - 1] == 0:     # 기준이 되는 숫자의 값을 변경
                sw_lst[B - 1] = 1
            else:
                sw_lst[B - 1] = 0

for i in range(len(sw_lst)):       # 20개씩 끊어서 출력
    if i % 10 == 9:
        print(sw_lst[i], end='\n')
    else:
        print(sw_lst[i], end=' ')