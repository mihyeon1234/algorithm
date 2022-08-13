n = int(input())

for i in range(1, 2 * n) :
    if i <= n :
        print((' '* (n - i)) + ('*' * ((2 * n - 1) - 2 * (n - i))))
    else :
        print((' '* (i - n)) + ('*' * ((2 * n - 1) - 2 * (i - n))))
