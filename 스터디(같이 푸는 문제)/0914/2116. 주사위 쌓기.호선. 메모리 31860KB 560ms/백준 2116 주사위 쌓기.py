import sys
sys.stdin = open('input.txt')

N = int(input())
M = 0
dice = []
for i in range(N):
    lst = list(map(int, input().split()))
    dice.append(lst)


def angry(up_dice, number):
    idx = 0
    for k in range(6):
        if number == up_dice[k]:
            idx = k
            break

    if idx == 0:
        return (max(up_dice[1], up_dice[2], up_dice[3], up_dice[4]), up_dice[5])
    elif idx == 5:
        return (max(up_dice[1], up_dice[2], up_dice[3], up_dice[4]), up_dice[0])
    elif idx == 1:
        return (max(up_dice[0], up_dice[2], up_dice[5], up_dice[4]), up_dice[3])
    elif idx == 3:
        return (max(up_dice[0], up_dice[2], up_dice[5], up_dice[4]), up_dice[1])
    elif idx == 2:
        return (max(up_dice[0], up_dice[1], up_dice[5], up_dice[3]), up_dice[4])
    elif idx == 4:
        return (max(up_dice[0], up_dice[1], up_dice[5], up_dice[3]), up_dice[2])


for i in range(1, 7):
    down_num = i
    answer = 0
    for j in range(N):
        total, down_num = angry(dice[j], down_num)
        answer += total
    if M < answer:
        M = answer
print(M)