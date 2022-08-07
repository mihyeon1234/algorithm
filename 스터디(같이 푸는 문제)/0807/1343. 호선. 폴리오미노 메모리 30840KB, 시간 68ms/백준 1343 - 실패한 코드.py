n = input()
nn = list(n)
if nn.count('X') % 2 == 1 :
    print(-1)
else :
    for i in range(3, len(n) + 1) :
        if nn[i-3 : i + 1] == ['X', 'X', 'X', 'X']:
            nn[i-3 : i + 1] = ['A', 'A', 'A', 'A']
    for i in range(1, len(n) + 1) :    
        if nn[i-1 : i + 1] == ['X', 'X']:
            nn[i-1 : i + 1] = ['B', 'B']
    ans = ''
    for i in nn :
        ans += i
    print(ans)

