n = int(input())
cnt = n
for i in range(n) :
    word = input()
    if len(word) != len(set(word)) :
        lst = []
        for j in word :
            if j in lst :
                if lst[-1] != j :
                    cnt -= 1
                    break
                else :
                    lst.append(j)
            else :
                lst.append(j)

print(cnt)