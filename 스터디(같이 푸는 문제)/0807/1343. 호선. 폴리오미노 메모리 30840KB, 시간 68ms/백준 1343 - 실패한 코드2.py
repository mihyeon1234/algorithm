n = input()
nn = list(n)
if nn.count('X') % 2 == 1 :
    print(-1)
else :
    i = n.replace('XXXX', 'AAAA')
    j = i.replace('XX', 'BB')
    print(j)