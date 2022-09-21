import sys
sys.stdin = open('input.txt')

N = int(input())
card = list(map(int, input().split()))
card.sort()
M = int(input())
trap_card = list(map(int, input().split()))
ans_card = []
for i in trap_card:
    start = 0
    end = N - 1
    while end - start != 1:
        mid = (start + end) // 2
        if i == card[end]:
            ans_card.append(1)
            break
        elif i == card[start]:
            ans_card.append(1)
            break
        else:
            if i == card[mid]:
                ans_card.append(1)
                break
            elif i > card[mid]:
                start = mid
            elif i < card[mid]:
                end = mid
    if end - start == 1:
        ans_card.append(0)
print(*ans_card)