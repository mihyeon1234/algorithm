# 방법 1
N = int(input())
li = list(map(int, input().split()))
ans = []
for i in range(N):                      #insert 내장함수 활용
    ans.insert(li[i], i + 1)
print(' '.join(map(str, ans[::-1])))


# 방법 2
N = int(input())
N_list = list(map(int, input().split()))
ans = [1]                               # 1은 기본값이므로 미리 입력
for i in range(1, len(N_list)):         # 1 이후의 값은 for문 활용
    ck_len = len(ans)                   # ans에 입력된 길이 확인
    if ck_len > N_list[i]:              # 넣을 위치가 입력된 길이보다 작으면 슬라이싱하여 추가
        ans = ans[ : N_list[i]] + [i + 1] + ans[N_list[i] : ck_len + 1]
    else:                               # 같거나 크면 제일 마지막에 위치하므로 그냥 추가
        ans += [i + 1]
ans.reverse()                           # 출력을 위해 reverse 진행
print(*ans)