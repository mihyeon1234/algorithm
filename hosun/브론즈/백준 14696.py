n = int(input())
for i in range(1, n + 1):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    A = a[1:]
    B = b[1:]
    A.sort()
    B.sort()

    while True :
        if A == B :
            print('D')
            break
        if A == [] :
            print('B')
            break
        if B == [] :
            print('A')
            break
        if max(A) > max(B) :
            print('A')
            break
        elif max(A) < max(B) :
            print('B')
            break
        else :
            if A.count(max(A)) > B.count(max(B)) :
                print('A')
                break
            elif A.count(max(A)) < B.count(max(B)) :
                print('B')
                break
            else :
                for i in range(A.count(max(A))) :
                    A.remove(max(A))
                    B.remove(max(B))

            
            