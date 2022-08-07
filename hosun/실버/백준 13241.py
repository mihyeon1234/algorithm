A, B = map(int, input().split())
C = min(A, B)
for i in range(C, -1, -1) :
    if A % i == 0 and B % i == 0 :
        print(int((A * B) / i)) 
        break
