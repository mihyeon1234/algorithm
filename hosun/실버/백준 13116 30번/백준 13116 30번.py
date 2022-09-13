import sys
sys.stdin = open('input.txt')


def f(n, m):                           # a, b의 부모 노드를 찾는 함수
    if n > m:                          # a가 b보다 크면 a는 부모 노드로 이동
        n //= 2
    elif n < m:                        # b가 a보다 크면 b는 부모 노드로 이동
        m //= 2
    else:                              # a와 b가 같으면 (해당 값 * 10)을 리턴
        return n * 10
    return f(n, m)                     # 반복


T = int(input())
for H in range(1, T + 1):
    a, b = map(int, input().split())
    print(f(a, b))
