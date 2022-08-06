lst = []
while True :
    A = list(map(int, input().split()))
    if A == [0, 0, 0] :
        break
    lst.append(A)
for i in lst :
    i.sort()
    if i[0]**2 + i[1]**2 == i[2]**2 :
        print('right')
    else :
        print('wrong')