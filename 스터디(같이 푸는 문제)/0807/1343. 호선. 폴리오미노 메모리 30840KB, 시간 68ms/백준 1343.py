n = input()
i = n.replace('XXXX', 'AAAA')
j = i.replace('XX', 'BB')
if 'X' in list(j) :
    print(-1)
else :
    print(j)