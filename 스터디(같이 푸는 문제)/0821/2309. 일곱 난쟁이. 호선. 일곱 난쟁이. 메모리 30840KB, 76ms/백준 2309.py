import sys
sys.stdin = open('input.txt')

lst = list(int(input()) for _ in range(9))
total = sum(lst)
for i in range(8):
    for j in range(i + 1, 9):
        if total - lst[i] - lst[j] == 100:
            del lst[j]
            del lst[i]
            break
    if len(lst) == 7:
        break
lst.sort()
for k in lst:
    print(k)
