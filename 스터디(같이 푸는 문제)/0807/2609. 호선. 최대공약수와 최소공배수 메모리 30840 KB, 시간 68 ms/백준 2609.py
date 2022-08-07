A, B = map(int, input().split()) # 최소공배수 = A 곱하기 B 나누기 최대공약수 
C = min(A, B)                       # 18
D = max(A, B)                       # 24
for i in range(C, 0, -1) :          # 18부터 아래로 하나씩 검사
    if D % i == 0 and C % i == 0 :  # i가 24와 18를을 모두 나누므로 최대공약수
        print(i)                    
        print(int(A * B / i))       # 최소공배수 = A 곱하기 B 나누기 최대공약수
        break                       # 최대공약수를 찾았으므로 멈춰!