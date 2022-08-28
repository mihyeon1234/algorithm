N = int(input())

result = []

for second in range(1, N + 1):
    angry = [N, second]
    first = N
    while True:
        third = first - second
        if third < 0:
            break
        angry.append(third)
        first = second
        second = third
    if len(result) < len(angry):
        result = angry
print(len(result))
print(*result)