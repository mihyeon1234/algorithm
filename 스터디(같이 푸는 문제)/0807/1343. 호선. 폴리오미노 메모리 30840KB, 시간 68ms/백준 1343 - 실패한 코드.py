n = input()
nn = list(n)

for i in range(3, len(n) + 1) :
    if nn[i-3 : i + 1] == ['X', 'X', 'X', 'X']:
        nn[i-3 : i + 1] = ['A', 'A', 'A', 'A']
for i in range(1, len(n) + 1) :    
    if nn[i-1 : i + 1] == ['X', 'X']:
        nn[i-1 : i + 1] = ['B', 'B']
ans = ''
for i in nn :
    ans += i

if 'X' in ans:
    print(-1)
else: 
    
    print(ans)

