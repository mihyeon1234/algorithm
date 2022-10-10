import sys
sys.stdin = open('input.txt')

T = int(input())
for H in range(T):
    N, word = input().split()
    ans = ''
    for i in word:
        ans += i * int(N)
    print(ans)