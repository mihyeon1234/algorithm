lst_1 = []
lst_2 = []
for i in range(3) :
    x, y = map(int, input().split())
    lst_1.append(x)
    lst_2.append(y)
lst_1.sort()
lst_2.sort()
if lst_1[0] == lst_1[1] and lst_2[0] == lst_2[1] :
    print (lst_1[2], lst_2[2])
elif lst_1[0] == lst_1[1] and lst_2[0] != lst_2[1] :
    print (lst_1[2], lst_2[0])
elif lst_1[0] != lst_1[1] and lst_2[0] != lst_2[1] :
    print (lst_1[0], lst_2[0])
elif lst_1[0] != lst_1[1] and lst_2[0] == lst_2[1] :
    print (lst_1[0], lst_2[2])