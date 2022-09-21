import sys
sys.stdin = open('input.txt')

M, N = map(int, input().split())
prime_number = []
for i in range(M, N + 1):
    if i == 1:
        continue
    elif i % 2 == 0:
        if i == 2:
            print(i)
        else:
            continue
    elif i % 3 == 0:
        if i == 3:
            print(i)
        else:
            continue
    elif i % 5 == 0:
        if i == 5:
            print(i)
        else:
            continue
    else:
        for j in range(2, round(i ** (1 / 2)) + 1):
            if i % j == 0:
                break
        else:
            print(i)