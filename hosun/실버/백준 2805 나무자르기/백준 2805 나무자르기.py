import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()


def f(x, y):
    start = 1
    end = y[-1]
    while start <= end:
        cuts = 0
        mid = (start + end) // 2
        for piece in y:
            if mid < piece:
                cuts += piece - mid
        if cuts == x:
            return mid
        elif cuts < x:
            end = mid - 1
        else:
            start = mid + 1
    return end


print(f(M, tree))