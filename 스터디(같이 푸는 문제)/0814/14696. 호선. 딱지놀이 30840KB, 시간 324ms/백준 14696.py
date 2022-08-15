n = int(input())
for i in range(1, n + 1):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    A = a[1:]            # 딱지의 그림부분 슬라이싱
    B = b[1:]            # 딱지의 그림부분 슬라이싱
    A.sort()
    B.sort()

    while True :
        if A == B :            # 둘이 같을 경우 무승부
            print('D')
            break
        if A == [] :            # A가 공집합일 경우 B의 승리
            print('B')
            break
        if B == [] :            # B가 공집합일 경우 B의 승리
            print('A')
            break
        if max(A) > max(B) :            # A의 최대값이 B의 최대값보다 클 경우 A의 승리
            print('A')
            break
        elif max(A) < max(B) :            # B의 최대값이 A의 최대값보다 클 경우 B의 승리
            print('B')
            break
        else :
            if A.count(max(A)) > B.count(max(B)) :    # A의 최대값과 B의 최대값이 동일할 때,
                print('A')                            # A의 수가 더 많으면 A의 승리
                break
            elif A.count(max(A)) < B.count(max(B)) :    # A의 최대값과 B의 최대값이 동일할 때,
                print('B')                              # B의 수가 더 많으면 A의 승리
                break
            else :                                      # A의 최대값과 B의 최대값이 동일할 때,
                for i in range(A.count(max(A))) :       # 둘의 개수도 동일하다면, 최대값 모두 삭제
                    A.remove(max(A))
                    B.remove(max(B))

            
            