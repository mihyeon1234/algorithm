import sys

K = int(sys.stdin.readline())
li = [0] * 100001                               # 값이 저장될 공간
last = -1
for _ in range(K):
    n = int(sys.stdin.readline())
    if n == 0:
        last -= 1                               # 0이 올 경우 마지막 위치 1 감소
    else:
        last += 1                               # 0이 아닐 경우 입력값 저장
        li[last] = n
print(sum(li[:last + 1]) if last != -1 else 0)  # last까지의 합을 구함. 만약 last가 -1이면 0 출력