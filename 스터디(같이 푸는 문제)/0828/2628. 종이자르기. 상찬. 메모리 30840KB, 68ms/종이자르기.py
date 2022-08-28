C, R = map(int, input().split())                # 입력받을 가로와 세로
T = int(input())
r_0 = []
c_1 = []
for _ in range(T):
    a, b = map(int, input().split())            # 자를 곳의 정보
    if a == 0:
        r_0.append(b)
    else:
        c_1.append(b)
r_0 = [0] + r_0 + [R]
c_1 = [0] + c_1 + [C]
r_0.sort()
c_1.sort()

maxV = 0
for i in range(1, len(r_0)):
    for j in range(1, len(c_1)):
        area = (r_0[i] - r_0[i - 1]) * (c_1[j] - c_1[j - 1])    # 자른 곳의 정보를 기준으로 면적구하기
        if area > maxV:
            maxV = area
print(maxV)