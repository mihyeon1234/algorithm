import sys
M, N = map(int, sys.stdin.readline().split())
num = [1] * (N + 1)                             # 에라토스테네스의 체를 활용할 저장공간
num[0] = num[1] = 0                             # 0과 1은 소수가 아니므로 0으로 저장
for i in range(2, N + 1):                       # 첫 소수인 2부터 시작
    if num[i] == 1:                             # 해당하는 숫자가 1이면
        if i >= M:                              # M보다 크거나 같을 때만 출력
            print(i)
        for j in range(2, (N // i) + 1):        # 그 이후의 배수는 모두 0으로 걸러준다.
            num[i * j] = 0