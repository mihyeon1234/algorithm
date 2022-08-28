import sys
sys.stdin = open('input.txt')

N1 = int(input())
result = []
for N2 in range(1, N + 1):
    lst = [N1, N2]
    NN = N1
    while True:
        N3 = NN - N2
        if N3 < 0:
            break
        lst.append(N3)
        NN = N2

