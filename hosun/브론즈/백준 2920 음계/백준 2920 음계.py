import sys
sys.stdin = open('input.txt')

answer = 'mixed'
num = input().split()
if num == ['1', '2', '3', '4', '5', '6', '7', '8']:
    answer = 'ascending'
elif num == ['8', '7', '6', '5', '4', '3', '2', '1']:
    answer = 'descending'
print(answer)