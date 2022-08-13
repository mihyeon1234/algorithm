A = []
B = []
for i in range(2) :  # 행렬을 두 번 받아야하므로
    N, M = map(int, input().split())
    if i == 0 :   # 첫 번째 행렬을 받으면
        for a in range(N) :  # A에 리스트로 추가
            A.append(list(map(int, input().split())))
    else :       # 두 번째 행렬을 받으면
        for b in range(N) :  # B에 리스트로 추가
            B.append(list(map(int, input().split())))
for i in A :     # A의 항목마다 B와 곱해주기 위해 추출
    lst = []
    for j in range(len(B[0])) : # B항목의 요소 수만큼 곱해야하므로
        X = 0
        for i_2 in range(len(i)) : # A항목의 요소 수만큼 곱해야하므로 
            X += i[i_2] * B[i_2][j]  # A항목의 요소와 B항목의 요소를 곱한 값을 X에 더해줌
        lst.append(X)                # X를 lst에 추가
    for k in lst :                   
        if k == lst[-1] :           # 다른 행에 출력하기 위해
            print (k)
        else :
            print(k, end = " ")     # 같은 행에 출력하기 위해
