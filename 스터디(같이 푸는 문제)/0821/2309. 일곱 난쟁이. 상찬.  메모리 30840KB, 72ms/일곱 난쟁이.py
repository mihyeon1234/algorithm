N = 9
people = [int(input()) for _ in range(N)]
#방법 1
result = []
for i in range(N - 7 + 1):
    for j in range(i + 1, N - 6 + 1):
        for k in range(j + 1, N - 5 + 1):
            for l in range(k + 1, N - 4 + 1):
                for m in range(l + 1, N - 3 + 1):
                    for n in range(m + 1, N - 2 + 1):
                        for o in range(n + 1, N - 1 + 1):
                            # print(i, j, k, l, m, n, o, end =' ')
                            # print()
                            if people[i] + people[j] + people[k] + people[l] + people[m] + people[n] + people[o] == 100:
                                result.append(people[i])
                                result.append(people[j])
                                result.append(people[k])
                                result.append(people[l])
                                result.append(people[m])
                                result.append(people[n])
                                result.append(people[o])
                                print(*sorted(result), sep= '\n')
                                exit()
#방법 2
subset = []
for i in range(1<<9):
    li = []
    for j in range(9):
        if i & (1<<j):
            li.append(people[j])
    if len(li) == 7:
        subset.append(li)

for k in subset:
    if sum(k) == 100:
        print(*sorted(k), sep = '\n')
        break

# 방법 3
# 조합을 사용하는 방법... 아직까지 모르겠음
