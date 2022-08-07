n = int(input())

lst = []                                    # 입력 값을 리스트로 담음
for i in range(n) :
    P = list(map(int, input().split()))
    lst.append(P)

f_lst = []
for i in lst :
    for j in range(i[0], i[0] + 10) :       # 3 ~ 13 까지
        for k in range(i[1], i[1] + 10) :   # 7 ~ 17 까지   
            f_lst.append((j, k))            # (3, 7) (3, 8) ... (4, 7) (4, 8)
                                            #... (13, 16) (13, 17) 이렇게 넓이에
                                            #  해당하는 영역의 좌표를 리스트에 담음
s_lst = set(f_lst)                          # 중복되는 좌표를 제거

print(len(s_lst))


