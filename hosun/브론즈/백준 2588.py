A = int(input())
B = input()
total = 0
for i in range(len(B) - 1, -1, -1) :
    print(A * int(B[i]))
    total += (A * int(B[i])) * (10**(len(B) - 1 - i))
print(total)
