n = int(input())

cnt = 0
for i in range(n) :
    if n % 5 == 0 :
        cnt += n // 5
        print(cnt)
        break
    else :
        if n < 0 :
            print(-1)
            break
        else :
            n -= 3
            cnt += 1




