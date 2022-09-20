import sys
from collections import deque                   # dq를 활용하면 훨씬 속도가 빠르다
                                                # append와 pop이 많을 경우 유리
n = int(sys.stdin.readline())
stack = deque()                                 # dq선언
last = 0                                        # 계속 1씩 증가할 자연수
result = deque()                                # dq선언
for i in range(n):
    data = int(sys.stdin.readline())
    if stack:                                   # stack에 숫자가 존재할 경우
        if stack[-1] <= data:                   # 마지막 숫자가 입력된 데이터보다 작거나 같을 경우에 실행이 가능
            while stack[-1] != data:            # 숫자가 같아질 때까지 stack에 더해준다
                last += 1
                stack.append(last)
                result.append('+')
            stack.pop()                         # 같아질 경우 stack의 마지막 숫자를 추출한다
            result.append('-')
        else:                                   # 입력데이터보다 stack의 마지막 숫자가 크면 수열을 만들 수 없다.
            print('NO')
            break
    else:
        if data >= last:                        # stack에 숫자가 없을 경우
            last += 1                           # data 입력값이 이제 넣어줄 숫자보다 커야 수열이 생성된다.
            stack.append(last)
            result.append('+')
            while stack[-1] != data:            # data 입력값과 같아질때까지 스택에 쌓아준다.
                last += 1
                stack.append(last)
                result.append('+')
            stack.pop()                         # 숫자가 같아졌을 경우 스택의 마지막 수를 추출한다.
            result.append('-')
        else:
            print('No')
            break
else:
    print('\n'.join(result))